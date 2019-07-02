# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class IngredientType(models.Model):
	typeName = models.CharField(max_length=255, unique = True) 
	
class PaymentType(models.Model):
	paymentTypeName = models.CharField(max_length=255, unique = True) # Ej: pago por gramos, por unidad, etc

class Ingredient(models.Model):
	name = models.CharField(max_length=255, unique = True) 
	ingredientType= models.ForeignKey(IngredientType, on_delete=models.PROTECT, blank = True, null = True)
	#paymentType = models.ForeignKey(PaymentType, on_delete=models.PROTECT)
	price = models.IntegerField()
	scale = models.IntegerField(default = 0)
	label = models.TextField(default ='')
	#criticalCondition= models.IntegerField()
	#durationTime = models.TimeField()
	#maxAmount = models.IntegerField()
	@property
	def generic_name(self):
		 "returns a generic name for the object, made of the local location and ingredient name"
		 return '%s' % (self.ingredient.name)
		 
		

	
# class Local(models.Model):
	# location = models.TextField()

# class IngredientLocal(models.Model):
	# ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT)
	# local = models.ForeignKey(Local, on_delete=models.PROTECT)
	# price = models.IntegerField()
	# current_amount = models.IntegerField()
	# offer_price = models.IntegerField()
	# @property
	# def generic_name(self):
		# "returns a generic name for the object, made of the local location and ingredient name"
		# return '%s' % (self.ingredient.name)

# class Entry(models.Model):
	# ingredientLocal = models.ForeignKey(IngredientLocal, on_delete=models.PROTECT)
	# amount = models.IntegerField()
	# timestamp = models.DateTimeField()

# class Discharge(models.Model):

	# ingredientLocal = models.ForeignKey(IngredientLocal, on_delete=models.PROTECT)
	# amount = models.IntegerField()
	# timestamp = models.DateTimeField()

class Purchase(models.Model):

	timestamp = models.DateTimeField(auto_now_add=True)
	totalPrice = models.IntegerField(default=0)


class Order(models.Model):

	purchase = models.ForeignKey(Purchase,related_name='orders', on_delete=models.PROTECT)
	orderPrice = models.IntegerField(default=0)
	name = models.TextField(default = 'defecto')
	#rfID = models.IntegerField()
	#ongoing = models.BooleanField(default = False)
	#receiving = models.PositiveIntegerField(default =0)
	
	#def save(self, *args, **kwargs):
		
	#	self.purchase.totalPrice += self.orderPrice
	#	super(Order, self).save(*args, **kwargs) 

class Item(models.Model):

	order = models.ForeignKey(Order,related_name='items', on_delete=models.PROTECT)
	ingredient = models.ForeignKey(Ingredient,related_name='items', on_delete=models.PROTECT)
	#amount = models.IntegerField()
	amount = models.FloatField()
	itemPrice = models.IntegerField()
	
	class Meta:
		unique_together = ["order", "ingredient"]
		
	def save(self, *args, **kwargs):
		
		self.order.orderPrice += self.itemPrice
			
		super(Item, self).save(*args, **kwargs)

# class GlobalAdmin(models.Model):
	# user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='globalAdmin')
	# def clean(self):
		# print("here")
		# if LocalUser.objects.filter(user=self.user).exists():
			# print("here2")
			# raise ValidationError("El usuario ya tiene un rol local asignado")

# class LocalUser(models.Model):
	# user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='localUser')
	# local = models.ForeignKey(Local,related_name='localUsers', on_delete=models.PROTECT)	
	# GLOBAL = 'G'
	# ADMIN = 'A'
	# KITCHEN = 'K'
	# SCRIPT = 'S'
	# JOB_CHOICES = ((ADMIN,'Local Admin'),(KITCHEN,'kitchen'),(SCRIPT,'script'),(GLOBAL,'global'))
	# job = models.CharField(max_length=1,choices=JOB_CHOICES)
#	def clean(self):
#		if GlobalAdmin.objects.filter(user=self.user).exists():
#			raise ValidationError("El usuario ya tiene un rol asignado")
#		if self.job == 'A' or self.job == 'K' or self.job == 'S' and self.local==null:
			

	
	


	
	

# Create your models here.
