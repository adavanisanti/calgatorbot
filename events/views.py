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
