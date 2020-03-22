from django.contrib import admin

# Register your models here.
from . models import Images
from . models import TextDescriptions
from . models import ImageDescriptions


admin.site.register(Images)
admin.site.register(TextDescriptions)
admin.site.register(ImageDescriptions)
