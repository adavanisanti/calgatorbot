from django.shortcuts import render

# Create your views here.
from rest_framework import generics,status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import EventSerializer, VenueSerializer
from .models import Event, Venue
import datetime

class EventAPIView(generics.ListCreateAPIView):
	queryset = Event.objects.all()
	serializer_class = EventSerializer


class VenueAPIView(generics.ListCreateAPIView):
	queryset = Venue.objects.all()
	serializer_class = VenueSerializer


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

	def create_slack_message_for_get_events_date(self):

		input_date = self.parameters['date']

		date = datetime.datetime.strptime(input_date, "%Y-%m-%d")

		fmt = '%b %d, %Y %-I:%M %p'
		fmt1 = '%-I:%M %p'

		events = Event.objects.filter(start_date__date=date)
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
