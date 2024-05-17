from rest_framework import serializers
from .models import Post
from django.contrib.auth.models import User
from .models import Content

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')

class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ['id', 'title', 'body', 'author', 'created_at', 'updated_at']
        read_only_fields = ['author', 'created_at', 'updated_at']