from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Product(models.Model):
	name = models.CharField(max_length=200)
	description = models.TextField(null=True, blank=True)
	image=models.ImageField(null=True,blank=True,upload_to="myimage")
	price = models.IntegerField(null=True, blank=True)

	def __str__(self):
		return self.name
    

class Order(models.Model):
	product = models.ForeignKey(Product, max_length=200, null=True, blank=True, on_delete = models.SET_NULL)
	created =  models.DateTimeField(auto_now_add=True) 

	def __str__(self):
		return self.product.name