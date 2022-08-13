from django.urls import path

from .views import  StoreListView, StoreDetailView


path('', StoreListView.as_view(), name="Store_list"),
path('<int:pk>/', StoreDetailView.as_view(), name='Store_detail'),