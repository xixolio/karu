from rest_framework import serializers
from cebolla.models import *
from django.contrib.auth.models import User

class IngredientTypeSerializer(serializers.ModelSerializer):
    	
	class Meta:
		model = IngredientType
		fields = ('id', 'typeName')

class PaymentTypeSerializer(serializers.ModelSerializer):
    	
	class Meta:
		model = PaymentType
		fields = ('id', 'paymentTypeName')

class IngredientSerializer(serializers.ModelSerializer):

	ingredientType = serializers.ReadOnlyField(source='ingredientType.typeName')
	paymentType = serializers.ReadOnlyField(source='paymentType.paymentTypeName')
	
	class Meta:
			model = Ingredient
			#fields = ('id', 'name','ingredientType','paymentType','criticalCondition','durationTime','maxAmount')
			fields = ('id', 'name','ingredientType','paymentType','price')

# class LocalSerializer(serializers.ModelSerializer):
    	
	# class Meta:
		# model = Local
		# fields = ('id', 'location')

# class IngredientLocalSerializer(serializers.ModelSerializer):
	
	# ingredient = serializers.ReadOnlyField(source='ingredient.name')
	# local = serializers.ReadOnlyField(source='local.location')
	# payment = serializers.ReadOnlyField(source='ingredient.paymentType.paymentTypeName')
	# ingredientType = serializers.ReadOnlyField(source='ingredient.ingredientType.typeName')
	# class Meta:
		# model = IngredientLocal
		# fields = ('id','ingredient','local','price','current_amount','offer_price','payment','ingredientType')

# class EntrySerializer(serializers.ModelSerializer):
	# ingredientLocal = serializers.ReadOnlyField(source='ingredientLocal.generic_name')
	# class Meta:
		# model = Entry
		# fields = ('amount','timestamp','ingredientLocal')
	
	

# class DischargeSerializer(serializers.ModelSerializer):
	# ingredientLocal = serializers.ReadOnlyField(source='ingredientLocal.generic_name')
	# class Meta:
		# model = Discharge
		# fields = ('amount','timestamp','ingredientLocal')
	
	# def create(self, validated_data):
		# amount = validated_data['amount']
		# ingredientLocal = validated_data['ingredientLocal']
		# ingredientLocal.current_amount += amount
		# ingredientLocal.save()
		# return Discharge.objects.create(**validated_data)

class ItemSerializerP(serializers.ModelSerializer):
	# gets object based on its primary key
	ingredient = serializers.SlugRelatedField(slug_field = 'name',queryset=Ingredient.objects.all())
	#itemPrice = serializers.IntegerField(read_only=True)
	class Meta:
		model = Item
		fields = ('ingredient','amount','itemPrice')
		
	# def create(self,validated_data):
		# ingredientLocalId = validated_data.pop('ingredientLocal')
		# itemPrice = IngredientLocal.objects.get(pk=ingredientLocalId).price
		# item = Item.objects.create(**validated_data, itemPrice=itemPrice)
		# return item

#Serializers used in order to create an entire purchase with orders and items
class OrderSerializerP(serializers.ModelSerializer):
#	algo = serializers.IntegerField()
	items = ItemSerializerP(many=True, required=True)
	orderPrice = serializers.IntegerField(read_only=True)
	class Meta:
		model = Order
		fields = ('orderPrice','cardId','items')
		
	def validate_items(self, items):
		if len(items) == 0:
			raise serializers.ValidationError('se requiere al menos un item')
		return items

class PurchaseSerializer(serializers.ModelSerializer):
#	local = serializers.ReadOnlyField(source='local.location')
#	local = serializers.PrimaryKeyRelatedField(queryset=Local.objects.all(),write_only=True)
	orders = OrderSerializerP(many=True)
	totalPrice = serializers.IntegerField(read_only=True)
	
	class Meta:
		model = Purchase
		fields = ('timestamp','orders','totalPrice')

	def create(self,validated_data):
	
		orders_data = validated_data.pop('orders')
#		print(validated_data)
		purchase = Purchase.objects.create(**validated_data)
		totalPrice = 0
		
		for order_data in orders_data:	
		
			items_data = order_data.pop('items')			
			order = Order.objects.create(purchase=purchase, **order_data)
			orderPrice = 0
			
			for item_data in items_data:
			
				itemPrice = item_data['itemPrice']
				amount = item_data['amount']
				orderPrice += itemPrice*amount
				Item.objects.create(order=order, itemPrice=itemPrice,**item_data)
				
			order.orderPrice = orderPrice
			totalPrice += orderPrice
			order.save()
		
		purchase.totalPrice = totalPrice
		purchase.save()
		
		return purchase
		
	def validate_orders(self, orders):
		if len(orders) == 0:
			raise serializers.ValidationError('se requiere al menos una compra')
		return orders

#class PurchaseSerializer(serializers.Serializer):
#	totalPrice = serializers.IntegerField()
#	localId = serializers.IntegerField()
#	orders = OrderSerializerP(many=True)
	
#	def create(self, validated_data):
#		localid = validated_data.pop('localId')
#		local=Local.objects.get(id=localid)
#		orders_data = validated_data.pop('orders')
#		print validated_data
#		purchase = Purchase.objects.create(local=local,**validated_data)
#		for order_data in orders_data:
#			order_data.pop('algo')
#			Order.objects.create(purchase=purchase, **order_data)
#		return purchase



class ItemSerializer(serializers.ModelSerializer):
	#order = serializers.ReadOnlyField(source='order.id')
	ingredient = serializers.ReadOnlyField(source='ingredient.name')
	class Meta:
		model = Item
		#fields = ('order','localIngredient','amount','itemPrice')
		fields = ('ingredient','amount','itemPrice')

class OrderSerializer(serializers.ModelSerializer):
	purchase = serializers.ReadOnlyField(source='purchase.id')	
	items = ItemSerializer(many=True, read_only=True)
	class Meta:
		model = Order
		fields = ('orderPrice','cardId','purchase','items')
		
# class LocalUserSerializer(serializers.ModelSerializer):
	# local = serializers.PrimaryKeyRelatedField(queryset=Local.objects.all())
	# job = serializers.CharField()
	# class Meta:
		# model = LocalUser
		# fields = ('job','local')
	
	# def validate(self,data):
		# "If the localUser job is K, S or A, but local was not provided, raise error"
		# if data['job'] != 'G' and 'local' not in data:
			# raise serializers.ValidationError("Para usuarios locales provea de informacion sobre el local donde trabaja")
		# jobs = ['J','K','S']
		# if data['job'] not in jobs:
			# raise serializers.ValidationError("Las posibles opciones son J, K y S")
		# "!!!AGREGAR!!! No two users can have the same job type and be related to the same local"
		# return data
			 

# class UserSerializer(serializers.ModelSerializer):
	   #email = serializers.EmailField()
	# password = serializers.CharField(write_only=True)
	# localUser = LocalUserSerializer()

	# class Meta:
		# model = User
		# fields = ('id', 'username','password','localUser')
	#fields = ('id', 'username','email','password')

	# def create(self,validated_data):
		# user = User.objects.create(username=validated_data['username'])
		# user.set_password(validated_data['password'])

		# user.save()
		# localUser_data = validated_data.pop('localUser') 
		# localUser = LocalUser.objects.create(user=user,**localUser_data)
		# return user




	

