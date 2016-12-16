from rest_framework import serializers

from .models import Event, Venue
from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)


class EventSerializer(TaggitSerializer,serializers.ModelSerializer):

	tags = TagListSerializerField()

	class Meta:
		model = Event
		fields = '__all__'


class VenueSerializer(serializers.ModelSerializer):

	class Meta:
		model = Venue
		fields = '__all__'
