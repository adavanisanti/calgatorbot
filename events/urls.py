from django.conf.urls import url
from django.conf.urls import include

from .views import (
	EventAPIView,
	VenueAPIView,
	EventRetrieveAPIView,
	VenueRetrieveAPIView,
	EventListAPIView,
	)

urlpatterns = [
	url(r'^events/$',EventAPIView.as_view(),name='events_api'),
	url(r'^events/(?P<pk>\d+)/$',EventRetrieveAPIView.as_view(),name='events_detail_api'),
	url(r'^venues/$',VenueAPIView.as_view(),name='venues_api'),
	url(r'^venues/(?P<pk>\d+)/$',VenueRetrieveAPIView.as_view(),name='venues_detail_api'),
	url(r'^webhook/$',EventListAPIView.as_view(),name='events_webhook_api'),
 ]
