from django.shortcuts import render

from rest_framework.generics import ListAPIView, RetrieveAPIView,ListCreateAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView
from .models import Store
from .serializers import StoreSerializer
# Create your views here.

class StoreListView(ListCreateAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

class StoreDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer