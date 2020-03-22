from . models import Images
from . models import TextDescriptions
from . models import ImageDescriptions
from rest_framework import viewsets, permissions
from .serializers import ImagesSerializer
from .serializers import TextDescriptionsSerializer
from .serializers import ImagesDescriptionsSerializer

class ImagesViewSet(viewsets.ModelViewSet):
	queryset = Images.objects.all()
	permission_classes = [
		permissions.AllowAny
	]
	serializer_class = ImagesSerializer

class TextDesriptionsViewSet(viewsets.ModelViewSet):
	queryset = TextDescriptions.objects.all()
	permission_classes = [
		permissions.AllowAny
	]
	serializer_class = TextDescriptionsSerializer

class ImageDescriptionsViewSet(viewsets.ModelViewSet):
	queryset = ImageDescriptions.objects.all()
	permission_classes = [
		permissions.AllowAny
	]
	serializer_class = ImagesDescriptionsSerializer