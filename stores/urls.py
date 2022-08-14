from django.urls import path

from .views import  StoreListView, StoreDetailView, PostListView, PostDetailView

urlpatterns = [
path('', StoreListView.as_view(), name="Store_list"),
path('<int:pk>/', StoreDetailView.as_view(), name='Store_detail'),
path('post/', PostListView.as_view(), name='post_list'),
path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
]