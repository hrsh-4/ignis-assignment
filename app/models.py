from django.db import models

# Create your models here.

class Event(models.Model):
	name = models.CharField(max_length = 300)
	time = models.DateTimeField(auto_now=False)
	price = models.PositiveIntegerField()
	image = models.URLField()

	def __str__(self):
		return self.name