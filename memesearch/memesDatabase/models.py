from django.db import models

# Create your models here.
class Images(models.Model):
	id = models.AutoField(primary_key = True, unique = True)
	image = models.URLField()
	vector = models.TextField()

	def __toStr__(this):
		return this.id

class TextDescriptions(models.Model):
	imageId = models.IntegerField()
	index = models.TextField()
	
	def __toStr__(this):
		return this.imageId

class ImageDescriptions(models.Model):
	imageId = models.IntegerField()
	index = models.TextField()
	
	def __toStr__(this):
		return this.ImageDescriptions