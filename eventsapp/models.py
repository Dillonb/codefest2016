from django.db import models

# Create your models here.


class Event(models.Model):
	"""A custom event model to represent events around UVM Campus"""
	USER = "U"
	CLUB = "C"
	USER_TYPES = (
		(USER, 'user'),
		(CLUB, 'club')
	)

	name = models.CharField(max_length=40)
	latitutde = models.FloatField()
	longitube = models.FloatField()
	user_type = models.CharField(max_length=1,choices=USER_TYPES)
	date_time = models.DateTimeField()


	user = models.FoerignKey("UVMUser")
