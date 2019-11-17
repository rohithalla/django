from django.db import models

# Create your models here.
class data(models.Model):
	name = models.CharField(max_length=40)
	id = models.IntegerField(primary_key=True)
	ph = models.IntegerField()

	def __str__(self):
		return self.id