from laundryshop.models import Shop
from rest_framework import viewsets, permissions

from .serializers import ShopSerializer

class ShopViewSet(viewsets.ModelViewSet):
	queryset = Shop.objects.all()

	permission_classes =[
		permissions.AllowAny
	]
	serializer_class = ShopSerializer