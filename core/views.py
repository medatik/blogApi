from django.shortcuts import render
from rest_framework import viewsets, permissions, generics, status
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from .models import User, Post, Comment, Like
from .serializers import UserSerializer, PostSerializer, CommentSerializer, LikeSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        if 'admin' in user.username.lower() or getattr(user, 'role', '') == 'admin':
            user.is_staff = True
            user.save()

class LogoutView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        try:
            return Response({
                "status": "success",
                "message": "Successfully logged out"
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "status": "error",
                "message": str(e)
            }, status=status.HTTP_400_BAD_REQUEST)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser] 

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        post = self.get_object()
        if post.author == self.request.user or self.request.user.is_staff:
            serializer.save()
        else:
            raise permissions.PermissionDenied("You can only edit your own posts.")
            
    def destroy(self, request, *args, **kwargs):
        post = self.get_object()
        if post.author == request.user or request.user.is_staff:
            self.perform_destroy(post)
            return Response({
                "status": "success",
                "message": "Post deleted successfully"
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                "status": "error",
                "message": "You can only delete your own posts"
            }, status=status.HTTP_403_FORBIDDEN)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({
            "status": "success",
            "message": "Comment created successfully",
            "data": serializer.data
        }, status=status.HTTP_201_CREATED)
        
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        
        
        if instance.user != request.user:
            return Response({
                "status": "error",
                "message": "You can only edit your own comments"
            }, status=status.HTTP_403_FORBIDDEN)
            
        
        if 'post' in request.data:
            del request.data['post']
            
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        
        return Response({
            "status": "success",
            "message": "Comment updated successfully",
            "data": serializer.data
        })
        
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        
        
        if instance.user != request.user:
            return Response({
                "status": "error",
                "message": "You can only delete your own comments"
            }, status=status.HTTP_403_FORBIDDEN)
            
        self.perform_destroy(instance)
        return Response({
            "status": "success",
            "message": "Comment deleted successfully"
        }, status=status.HTTP_200_OK)

class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        
        post_id = self.request.data.get('post')
        if Like.objects.filter(user=self.request.user, post_id=post_id).exists():
            raise ValidationError("You have already liked this post")
        serializer.save(user=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            self.perform_create(serializer)
            return Response({
                "status": "success",
                "message": "Post liked successfully",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        except serializers.ValidationError as e:
            return Response({
                "status": "error",
                "message": str(e.detail[0])
            }, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.user != request.user:
            return Response({
                "status": "error",
                "message": "You can only remove your own likes"
            }, status=status.HTTP_403_FORBIDDEN)
            
        self.perform_destroy(instance)
        return Response({
            "status": "success",
            "message": "Like removed successfully"
        }, status=status.HTTP_200_OK)
