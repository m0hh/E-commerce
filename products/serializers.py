from rest_framework import serializers
from .models import *
from rest_framework.authtoken.models import Token

# Products serializer with a read only field for the field and user
class ProductSerializer(serializers.HyperlinkedModelSerializer):
    seller = serializers.ReadOnlyField(source = 'seller.username')
    class Meta:
        model = Product
        fields = ['url','id', 'title', 'description','image', 'price', 'quantity', 'seller', 'date']
        read_only_fields = ['date', 'seller']


#orders serializer with read only fields for the user
#I also overrode the create function to subtract the quantity orderd from the quantity in my model and also to create an OrderState instance
# Also I overrode the update function to subtract the quantity updated of a given order from the Order object
# Note that you can't order a quantity greater than that of the avaliable in the object

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source = 'user.username')
    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ['user']

    def create(self, validated_data):
        order = Order(**validated_data)
        if order.item.quantity - order.quantity < 0:
            raise serializers.ValidationError('There is not enough items')
        order.item.quantity -= order.quantity
        order.item.save()
        order.save()
        state = OrderState(state=1, order= order, owner = order.item.seller, buyer= order.user)
        state.save()
        return order
    
    def update(self,instance, validated_data):
        order = instance
        original_quantity = order.item.quantity + order.quantity

        order.item = validated_data.get('item', order.item)
        order.payment_options =validated_data.get('payment_options', order.payment_options)
        order.Delivery = validated_data.get('Delivery', order.Delivery)
        order.quantity = validated_data.get('quantity', order.quantity)

        if original_quantity - validated_data.get('quantity') < 0:
            raise serializers.ValidationError('There is not enough items')
        order.item.quantity = original_quantity - validated_data.get('quantity')
        order.item.save()
        order.save()
        return order


# simple cart serialzer with a read only field for user 
class CartSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source = 'user.username')
    class Meta:
        model = Cart
        fields = '__all__'
        read_only_fields = ['user']

#simple Order state serializer with a read only fields for the order, owner and buyer
class StateSerializer(serializers.HyperlinkedModelSerializer):
    order = serializers.ReadOnlyField(source = 'order.item.title')
    owner = serializers.ReadOnlyField(source = 'owner.username')
    buyer = serializers.ReadOnlyField(source = 'buyer.username')


    class Meta:
        model = OrderState
        fields = '__all__'
        read_only_fields = ['order', 'owner', 'buyer']

#user serializer with an overrode create function to register new users and generating Tokens for the
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        Token.objects.create(user=user)
        return user