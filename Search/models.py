from django.db import models

class Search_Websites(models.Model):
	name = models.CharField(max_length = 128)
	url = models.CharField(max_length = 128)
	mid = models.IntegerField()
	types = models.CharField(max_length = 256)
	def __str__(self):              # __unicode__ on Python 2
		return self.name

# Create your models here.