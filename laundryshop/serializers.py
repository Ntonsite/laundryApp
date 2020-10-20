from rest_framework import serializers
from laundryshop.models import Shop

class ShopSerializer(serializers.ModelSerializer):

	class Meta:
		model = 'Shop'
		fields = '__all__'
