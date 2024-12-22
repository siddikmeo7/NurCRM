# views.py
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ClientListCreateAPIView(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ClientRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class TransactionListCreateAPIView(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def perform_create(self, serializer):
        client = Client.objects.get(id=self.kwargs['client_id'])
        serializer.save(client=client, user=self.request.user)

class TransactionRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class ProfileRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

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

