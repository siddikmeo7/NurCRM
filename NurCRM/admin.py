from django.contrib import admin
from .models import *

# Registering Custom User model
admin.site.register(CustomUser)

# Registering Client model
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'last_name', 'phone_number', 'email', 'balance', 'is_active', 'created_at', 'updated_at']
    search_fields = ['name', 'last_name', 'phone_number', 'email']
    list_filter = ['is_active', 'created_at']

# Registering Profile model
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'bio', 'profile_picture', 'website', 'date_of_birth', 'is_active', 'created_at', 'updated_at']
    search_fields = ['user__username', 'user__email']
    list_filter = ['is_active', 'created_at']

# Registering Product model
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'index', 'category', 'colour', 'price', 'cost_price', 'up_to', 'sold', 'is_active', 'created_at']
    search_fields = ['title', 'index', 'category__name', 'colour__name']
    list_filter = ['category', 'colour', 'is_active']

# Registering Category model
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active']
    search_fields = ['name']
    list_filter = ['is_active']

# Registering Colour model
@admin.register(Colour)
class ColourAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active']
    search_fields = ['name']
    list_filter = ['is_active']

# Registering Sklad model (Warehouse)
@admin.register(Sklad)
class SkladAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active']
    search_fields = ['name']
    list_filter = ['is_active']

# Registering SkladProduct model (Warehouse products)
@admin.register(SkladProduct)
class SkladProductAdmin(admin.ModelAdmin):
    list_display = ['sklad', 'product', 'quantity', 'is_active']
    search_fields = ['sklad__name', 'product__title']
    list_filter = ['is_active']

# Registering Order model
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['client', 'product', 'quantity', 'price_at_purchase', 'total_price', 'status', 'created_at']
    search_fields = ['client__name', 'product__title']
    list_filter = ['status', 'created_at']

# Registering Transaction model
@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['client', 'transaction_type', 'amount', 'created_at']
    search_fields = ['client__name']
    list_filter = ['transaction_type', 'created_at']

# Registering ShopCategory model
@admin.register(ShopCategory)
class ShopCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    search_fields = ['name']
    list_filter = ['created_at']

# Registering ShopProduct model
@admin.register(ShopProduct)
class ShopProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'stock', 'user', 'is_active', 'created_at']
    search_fields = ['name', 'category__name', 'user__username']
    list_filter = ['category', 'is_active', 'created_at']

# Registering CartItem model
@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['product', 'quantity', 'user', 'is_active', 'created_at']
    search_fields = ['product__name', 'user__username']
    list_filter = ['is_active', 'created_at']

# Registering ShopOrder model
@admin.register(ShopOrder)
class ShopOrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'status', 'total_price', 'created_at']
    search_fields = ['user__username']
    list_filter = ['status', 'created_at']

# Registering TransactionOrder model
@admin.register(TransactionOrder)
class TransactionOrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'client', 'transaction_type', 'amount', 'created_at']
    search_fields = ['user__username', 'client__name']
    list_filter = ['transaction_type', 'created_at']
