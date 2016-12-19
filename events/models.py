from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

from django.core.validators	import MinValueValidator,MaxValueValidator,MaxLengthValidator, RegexValidator
from taggit.managers import TaggableManager


class Venue(models.Model):
	YES_NO_CHOICES = ((None,''), (True,'Yes'), (False, 'No'))

	name = models.CharField(_("name"),max_length=255,blank=False)
	street1 = models.CharField(_("street1"),max_length=255,blank=False)
	street2 = models.CharField(_("street2"),max_length=255,blank=True,default='')
	city = models.CharField(_("city"),max_length=255,blank=False)
	state = models.CharField(_("state"),max_length=255,blank=False)
	zipcode = models.PositiveIntegerField(validators=[MinValueValidator(10000),MaxValueValidator(99999)])
	wifi = models.NullBooleanField(choices=YES_NO_CHOICES,max_length=3,blank=True, null=True, default=None)
	mapurl = models.URLField(_("mapurl"),default='',blank=True)
	venueurl = models.URLField(_("venueurl"),default='',blank=True)
	venueid = models.PositiveIntegerField(_("venueid"),null=True)

	def __str__(self):
		return self.name


# Create your models here.
class Event(models.Model):
	title = models.CharField(_("title"), max_length=255)
	description = models.TextField(_("description"))
	start_date = models.DateTimeField(verbose_name=_("start date"))
	end_date = models.DateTimeField(_("end date"))
	website = models.URLField(_("website"),default='',blank=True)
	venue_details = models.TextField(_("venue_details"),default='',blank=True)
	venue = models.ForeignKey(Venue,blank=True,null=True)
	tags = TaggableManager(blank=True)
	feed_id = models.CharField(_("feed_id"),max_length=255,blank=True,null=True)
	event_ics = models.URLField(_("website"),default='',blank=True)

	def __str__(self):
		return self.title
    
