from django.shortcuts import render

# Create your views here.
from rest_framework import generics,status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import EventSerializer, VenueSerializer
from .models import Event, Venue
from django_filters.rest_framework import DjangoFilterBackend

import datetime
from pytz import timezone
import pytz

class EventAPIView(generics.ListCreateAPIView):
	queryset = Event.objects.all()
	serializer_class = EventSerializer
	filter_backends = (DjangoFilterBackend,)
	filter_fields = ('feed_id',)


class VenueAPIView(generics.ListCreateAPIView):
	queryset = Venue.objects.all()
	serializer_class = VenueSerializer
	filter_backends = (DjangoFilterBackend,)
	filter_fields = ('venueurl',)

class EventRetrieveAPIView(generics.RetrieveUpdateAPIView):
	queryset = Event.objects.all()
	serializer_class = EventSerializer


class VenueRetrieveAPIView(generics.RetrieveUpdateAPIView):
	queryset = Venue.objects.all()
	serializer_class = VenueSerializer

class EventListAPIView(APIView):


	def post(self,request,format=None):

		print request.data

		try:
			self.action = request.data['result']['action']
			self.parameters = request.data['result']['parameters']
		except:
			self.action = 'show.schedule'
			self.parameters = {}

		return Response(self.get_slack_message(),status=status.HTTP_200_OK)


	def get_slack_message(self):

		slack_message = self.create_slack_message()
		# slack_message = {}
		
		slack_final_data = {
			"speech" : "Today is a good day",
			"dispayText" : "Today is a good day",
			"data": {"slack": slack_message},
			"source" : "apiai-eventsbot1-webhook-sample",
		}

		return slack_final_data

	def create_slack_message(self):

		if self.action == 'get.events':
			slack_message = self.create_slack_message_for_get_events()
		elif self.action == 'get.events.date':
			slack_message = self.create_slack_message_for_get_events_date()
		else:
			slack_message = {}


		return slack_message

	def create_slack_message_for_get_events(self):

		fmt = '%b %d, %Y %-I:%M %p'
		fmt1 = '%-I:%M %p'

		events = Event.objects.all()
		fields = []
		for event in events:
			item = {}
			item['title'] = event.title

			if event.start_date.date() == event.end_date.date():
				end_fmt = fmt1
			else:
				end_fmt = fmt

			item['value'] = event.start_date.strftime(fmt) + ' to ' + event.end_date.strftime(end_fmt)
			item['short'] = 'true'
			fields.append(item)
		
		slack_message = {
			"text" : "Below is the schedule  ",
			"attachments" : [
				{
					"title" : "Calgator",
					"title_link" : "www.calgator.org",
					"color" : "#36a64f",
					"fields" : fields,
				}
			],
		}

		return slack_message

	def get_slack_message_fields(self,events):

		fmt = '%b %d, %Y %-I:%M %p'
		fmt1 = '%-I:%M %p'

		fields = []
		for event in events:
			item = {}
			item['title'] = event.title
			start_date_time = event.start_date.astimezone(timezone('US/Pacific'))
			end_date_time   = event.end_date.astimezone(timezone('US/Pacific'))

			if start_date_time.date() == end_date_time.date():
				end_fmt = fmt1
			else:
				end_fmt = fmt
			
			start_time = start_date_time.strftime(fmt)
			end_time = end_date_time.strftime(end_fmt)

			item['value'] =  start_time + ' to ' + end_time
			item['short'] = 'true'
			fields.append(item)

		slack_message = {
			"text" : "Below is the schedule  ",
			"attachments" : [
				{
					"title" : "<www.calgator.org|Calgator>",
					"title_link" : "www.calgator.org",
					"color" : "#36a64f",
					"fields" : fields,
				}
			],
		}

		return slack_message

	def create_slack_message_for_get_events_date(self):

		input_date = self.parameters['date']

		date = datetime.datetime.strptime(input_date, "%Y-%m-%d")
		events = Event.objects.filter(start_date__date=date).order_by('start_date')

		return self.get_slack_message_fields(events)
		
