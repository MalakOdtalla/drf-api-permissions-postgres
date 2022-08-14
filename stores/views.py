from django.shortcuts import render

from rest_framework.generics import ListAPIView, RetrieveAPIView,ListCreateAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView
from .models import Store,Post
from .serializers import StoreSerializer
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrReadOnly
from .serializers import StoreSerializer, PostSerializer
# Create your views here.

class StoreListView(ListCreateAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

class StoreDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = [IsOwnerOrReadOnly]

class PostListView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class PostDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]