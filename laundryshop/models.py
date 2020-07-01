from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Shop(models.Model):
	name         = models.CharField(max_length=100)
	description  = models.TextField()
	latitude     = models.FloatField()
	longitude    = models.FloatField()
	image        = models.ImageField(blank=True, upload_to='laundryshop')
	location     = models.CharField(max_length=50)
	owner        = models.ForeignKey(User, on_delete=models.CASCADE)

	AVAILABLE    = 'AV'
	CLOSED       = 'CO'

	STATUS   = [
		(AVAILABLE, 'Available'),
		(CLOSED, 'Closed'),
	]

	status = models.CharField(choices=STATUS, max_length=2, default=AVAILABLE)

	def __str__(self):
		return self.name
 
class Product(models.Model):
	name = models.CharField(max_length=50)
	description= models.TextField()
	price = models.IntegerField()
	shop = models.ForeignKey(Shop, on_delete=models.CASCADE)

	def __str__(self):
		return self.name


class Order(models.Model):
	shop         = models.ForeignKey(Shop, on_delete=models.CASCADE)
	customerName = models.CharField(max_length=50)
	phone        = models.IntegerField()
	email        = models.EmailField()
	product      = models.ForeignKey(Product, on_delete=models.CASCADE)
	date_ordered  = models.DateTimeField(default=timezone.now)
	date_event   = models.DateTimeField()
	ordered_by    = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.customerName