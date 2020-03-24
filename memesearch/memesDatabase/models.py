from django.db import models

# Create your models here.
class Images(models.Model):
	id = models.AutoField(primary_key = True, unique = True)
	image = models.URLField()
	vector = models.TextField()

	def __toStr__(this):
		return "toStr"

class TextDescriptions(models.Model):
	# image = models.ForeignKey(Images, on_delete=models.CASCADE)
	word = models.TextField(unique=True)
	index = models.TextField()
	
	def __toStr__(this):
		return this.index

class ImageDescriptions(models.Model):
	# image = models.ForeignKey(Images, on_delete=models.CASCADE)
	word = models.TextField(unique=True)
	index = models.TextField()
	
	def __toStr__(this):
		return this.index