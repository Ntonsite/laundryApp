from rest_framework import routers
from .api import ShopViewSet

router = routers.DefaultRouter()
router.register('api/shops', ShopViewSet, 'shops')

urlpatterns = router.urls