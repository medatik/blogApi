# core/serializers.py
from rest_framework import serializers
from .models import User, Post, Comment, Like

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'role']
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'required': True}
        }
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        if validated_data.get('role') == 'admin':
            user.is_staff = True
            user.is_superuser = True
            user.save()
        return user

class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'created_at', 'is_published', 'author']

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    
    class Meta:
        model = Comment
        fields = ['id', 'text', 'created_at', 'post', 'user']
        extra_kwargs = {
            'post': {'required': False}  # Make post field optional for updates
        }

class LikeSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    
    class Meta:
        model = Like
        fields = ['id', 'post', 'user']
