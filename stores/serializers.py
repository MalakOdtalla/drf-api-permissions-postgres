from rest_framework import serializers

from .models import Store,Post
from django.contrib.auth import get_user_model

class StoreSerializer(serializers.ModelSerializer):
    owner_name = serializers.CharField(source='owner', read_only=True)

    class Meta:
        model = Store
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["username", "email"]