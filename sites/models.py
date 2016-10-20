from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Site(models.Model):

	user = models.ForeignKey(User, related_name='site')
	site_name = models.CharField(max_length=100)
	address = models.CharField(max_length=100)
	description = models.CharField(max_length=500)
	date_created = models.DateTimeField(auto_now_add=True)
	date_updated = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.site_name
