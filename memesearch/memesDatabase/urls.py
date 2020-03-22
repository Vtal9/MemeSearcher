from rest_framework import routers
from .api import ImagesViewSet
from .api import TextDesriptionsViewSet
from .api import ImageDescriptionsViewSet

router = routers.DefaultRouter()
router.register('api/images', ImagesViewSet, 'Images')
router.register('api/textDescriptions', TextDesriptionsViewSet, 'textDescriptions')
router.register('api/imageDescriptions', ImageDescriptionsViewSet, 'imageDescriptions')
urlpatterns = router.urls
