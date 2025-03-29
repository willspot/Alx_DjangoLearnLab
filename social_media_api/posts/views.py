from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.views import APIView
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticated
from notifications.models import Notification
from rest_framework.response import Response

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


class FeedView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]  # Ensure the user is authenticated

    def get_queryset(self):
        # Get the current authenticated user
        current_user = self.request.user
        
        # Get posts from users that the current user is following
        followed_users = current_user.following.all()
        # Add the current user to the queryset so they see their own posts as well
        followed_users = followed_users | current_user  # Including the current user in the feed
        
        # Fetch posts from followed users, ordered by creation date (most recent first)
        return Post.objects.filter(author__in=followed_users).order_by('-created_at')

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)


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


# View to Like a Post
class LikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        # Get the Post object
        post = get_object_or_404(Post, pk=pk)

        # Ensure the user cannot like their own post (Optional)
        if post.author == request.user:
            return Response({"detail": "You cannot like your own post."}, status=status.HTTP_400_BAD_REQUEST)

        # Check if the user has already liked the post
        like, created = Like.objects.get_or_create(user=request.user, post=post)

        if created:
            # If the like was successfully created, generate a notification
            Notification.objects.create(
                recipient=post.author,  # Post owner
                actor=request.user,  # User who liked the post
                verb="liked",
                target=post,
                timestamp=like.created_at
            )
            return Response({"detail": "Post liked successfully."}, status=status.HTTP_201_CREATED)
        else:
            return Response({"detail": "You have already liked this post."}, status=status.HTTP_400_BAD_REQUEST)

# View to Unlike a Post
class UnlikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        # Get the Post object
        post = get_object_or_404(Post, pk=pk)

        # Check if the user has liked the post
        try:
            like = Like.objects.get(user=request.user, post=post)
        except Like.DoesNotExist:
            return Response({"detail": "You have not liked this post."}, status=status.HTTP_400_BAD_REQUEST)

        # Delete the like
        like.delete()

        # Create a notification for unliking (optional)
        Notification.objects.create(
            recipient=post.author,  # Post owner
            actor=request.user,  # User who unliked the post
            verb="unliked",
            target=post,
            timestamp=None  # Can leave timestamp blank or set it to the current time
        )

        return Response({"detail": "Post unliked successfully."}, status=status.HTTP_200_OK)