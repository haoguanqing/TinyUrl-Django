from django.db import models
from django.utils import timezone

class UrlModel(models.Model):
	short_url = models.CharField(max_length=32)
	long_url = models.CharField(max_length=300)
	timestamp = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.short_url + ' --> ' + self.long_url