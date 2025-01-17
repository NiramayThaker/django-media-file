from django.db import models


# Create your models here.
class Dog(models.Model):
	name = models.CharField(max_length=64)
	image = models.ImageField(upload_to='dogs/')

	# Can use django-clean lib.
	def delete(self):
		self.image.delete()
		super().delete()
