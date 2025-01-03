# urls.py
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'products', ShopProductViewSet, basename='shopproduct')
router.register(r'orders', ShopOrderViewSet, basename='shoporder')

urlpatterns = [
    path('products/', ProductListCreateAPIView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(), name='product-retrieve-update-destroy'),
    path('clients/', ClientListCreateAPIView.as_view(), name='client-list-create'),
    path('clients/<int:pk>/', ClientRetrieveUpdateDestroyAPIView.as_view(), name='client-retrieve-update-destroy'),
    path('clients/<int:client_id>/transactions/', TransactionListCreateAPIView.as_view(), name='transaction-list-create'),
    path('transactions/<int:pk>/', TransactionRetrieveUpdateDestroyAPIView.as_view(), name='transaction-retrieve-update-destroy'),
    path('profile/', ProfileRetrieveUpdateAPIView.as_view(), name='profile-retrieve-update'),
    path('categories/', CategoryListCreateAPIView.as_view(), name='category-list-create'),
    path('colours/', ColourListCreateAPIView.as_view(), name='colour-list-create'),
    path('sklads/', SkladListCreateAPIView.as_view(), name='sklad-list-create'),
    path('sklad-products/', SkladProductListCreateAPIView.as_view(), name='sklad-product-list-create'),
    path('shop/', include(router.urls)),
    # For Server Render
    path('', run_migrations, name='run_migrations'),
]
