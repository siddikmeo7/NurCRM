# views.py
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *

CustomUser = get_user_model()

class CustomUserCreateAPIView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Filter products to only show those created by the authenticated user
        return Product.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ClientListCreateAPIView(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def get_queryset(self):
        # Filter clients to only show those related to the authenticated user
        return Client.objects.filter(user=self.request.user)  # <-- Change `Product` to `Client`
    
    def perform_create(self, serializer):
        # Assign the authenticated user to the client before saving
        serializer.save(user=self.request.user)

class ClientRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

from django.core.mail import send_mail
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status

class TransactionListCreateAPIView(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def get_queryset(self):
        # Filter transactions to only show those related to the authenticated user
        return Transaction.objects.filter(client__user=self.request.user)

    def perform_create(self, serializer):
        # Get the client associated with the transaction
        client = Client.objects.get(id=self.kwargs['client_id'])

        # Save the transaction
        transaction = serializer.save(client=client, user=self.request.user)

        # Send email to client after transaction is created
        self.send_transaction_email(client)

    def send_transaction_email(self, client):
        subject = 'Transaction Confirmation'
        message = f'Hello {client.name},\n\nYour transaction has been successfully processed.'
        recipient_list = [client.user.email]

        send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list)

    def create(self, request, *args, **kwargs):
        # Override to include the response
        response = super().create(request, *args, **kwargs)
        return response


class TransactionRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class ProfileRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get_queryset(self):
        # Filter to ensure user can only modify their own products
        return Product.objects.filter(user=self.request.user)

    def get_object(self):
        return self.request.user.profile 

class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ColourListCreateAPIView(generics.ListCreateAPIView):
    queryset = Colour.objects.all()
    serializer_class = ColourSerializer

class SkladListCreateAPIView(generics.ListCreateAPIView):
    queryset = Sklad.objects.all()
    serializer_class = SkladSerializer


class SkladProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = SkladProduct.objects.all()
    serializer_class = SkladProductSerializer

# Shop Part

# ShopOrder views
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action

class ShopProductViewSet(viewsets.ModelViewSet):
    queryset = ShopProduct.objects.all()
    serializer_class = ShopProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['post'])
    def add_to_cart(self, request, pk=None):
        product = self.get_object()
        quantity = request.data.get('quantity')
        if quantity > product.stock:
            return Response({'error': 'Quantity exceeds stock'}, status=400)
        
        cart_item = CartItem.objects.create(product=product, quantity=quantity, user=request.user)
        return Response(CartItemSerializer(cart_item).data)

class ShopOrderViewSet(viewsets.ModelViewSet):
    queryset = ShopOrder.objects.all()
    serializer_class = ShopOrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        cart_items = request.data.get('cart_items')
        total_price = sum(item['product']['price'] * item['quantity'] for item in cart_items)
        order = ShopOrder.objects.create(user=request.user, total_price=total_price, status='pending')

        for item_data in cart_items:
            product = item_data['product']
            quantity = item_data['quantity']
            CartItem.objects.create(product=product, quantity=quantity, user=request.user)
            order.cart_items.add(item_data['id'])

        return Response(ShopOrderSerializer(order).data)

