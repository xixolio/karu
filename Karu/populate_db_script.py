from cebolla.models import *
#import numpy as np

if not IngredientType.objects.filter(typeName = 'vegetal').exists():

	IngredientType.objects.create(typeName = 'vegetal')

if not PaymentType.objects.filter(paymentTypeName = 'por gramo').exists():

	PaymentType.objects.create(paymentTypeName = 'por gramo')

ingredients = ['cebolla','tomate','palta','pimenton']
prices = [10]*len(ingredients)

vegetal = IngredientType.objects.get(typeName = 'vegetal')
gramo = PaymentType.objects.get(paymentTypeName = 'por gramo')

for ingredient,price in zip(ingredients, prices):
	
	if not Ingredient.objects.filter(name = ingredient).exists():
		Ingredient.objects.create(name = ingredient, price = price, ingredientType = vegetal, paymentType = gramo)

ingredient = Ingredient.objects.get(name = ingredients[0])
purchase = Purchase.objects.create()
order = Order.objects.create(purchase = purchase, cardId = 1)
Item.objects.create(ingredient = ingredient, order = order, amount = 50, itemPrice = 10)

