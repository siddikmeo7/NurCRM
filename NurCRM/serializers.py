# serializers.py
from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'email', 'phone_number']

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        # No need to manually create the profile since the signal will do it
        return user

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'index', 'category', 'colour', 'price', 'cost_price', 'sold', 'up_to', 'is_active', 'created_at', 'user']


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'name', 'last_name', 'phone_number', 'email', 'address', 'balance', 'created_at', 'updated_at', 'is_active']


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'transaction_type', 'amount', 'comments', 'client', 'user', 'created_at']

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'bio', 'profile_picture', 'website', 'date_of_birth', 'user']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class ColourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colour
        fields = ['id', 'name']

class SkladSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sklad
        fields = ['id', 'name']

class SkladProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkladProduct
        fields = ['id', 'sklad', 'product', 'quantity']


# Shop Part
class ShopCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopCategory
        fields = ['id', 'name']

class ShopProductSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=ShopCategory.objects.all())
    user = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())

    class Meta:
        model = ShopProduct
        fields = '__all__'

    def create(self, validated_data):
        # Extract the nested fields
        category_data = validated_data.pop('category')
        user_data = validated_data.pop('user')

        # You can either create a new instance for nested fields if needed
        category = ShopCategory.objects.get(id=category_data.id)
        user = CustomUser.objects.get(id=user_data.id)

        # Create the ShopProduct instance
        shop_product = ShopProduct.objects.create(category=category, user=user, **validated_data)
        
        return shop_product

class CartItemSerializer(serializers.ModelSerializer):
    product = ShopProductSerializer()

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity', 'user']

class ShopOrderSerializer(serializers.ModelSerializer):
    cart_items = CartItemSerializer(many=True)

    class Meta:
        model = ShopOrder
        fields = ['id', 'user', 'cart_items', 'total_price', 'status', 'created_at']
