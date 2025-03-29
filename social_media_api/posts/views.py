from django.shortcuts import render
from rest_framework import viewsets
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticated

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


@api_view(['GET'])
def user_feed(request):
    followed_users = request.user.following.all()
    posts = Post.objects.filter(author__in=followed_users).order_by('-created_at')
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def like_post(request, post_id):
    post = Post.objects.get(id=post_id)
    Like.objects.create(post=post, user=request.user)
    return Response({"message": "Post liked"})
