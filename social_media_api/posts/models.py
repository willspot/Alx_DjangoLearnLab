from django.db import models
from accounts.models import CustomUser

class Post(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

class Notification(models.Model):
    recipient = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    actor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='actor')
    verb = models.CharField(max_length=255)
    target = models.GenericForeignKey('content_type', 'object_id')
    timestamp = models.DateTimeField(auto_now_add=True)
