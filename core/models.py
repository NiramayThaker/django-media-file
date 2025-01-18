from django.db import models
from django.core.validators import FileExtensionValidator

ext_validator = FileExtensionValidator(['png', 'jpg', 'pdf'])

# Create your models here.
class Dog(models.Model):
	name = models.CharField(max_length=64)
	image = models.FileField(upload_to='dogs/', validators=[ext_validator])

	# Can use django-clean lib.
	def delete(self):
		self.image.delete()
		super().delete()
