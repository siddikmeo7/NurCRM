# serializers.py
from rest_framework import serializers
from .models import Product, Client, Transaction, Profile, Category, Colour, Sklad, SkladProduct

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'index', 'category', 'colour', 'price', 'cost_price', 'sold', 'up_to', 'is_active', 'created_at', 'user']

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'name', 'phone_number', 'email', 'address', 'balance', 'user']

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['client', 'product', 'quantity', 'price_at_purchase', 'total_price', 'status']

    def validate(self, data):
        if data['quantity'] > data['product'].stock:
            raise serializers.ValidationError('Quantity exceeds available stock.')
        return data


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