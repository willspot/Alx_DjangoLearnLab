from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    bio = models.TextField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='followers')

    def __str__(self):
        return self.username

    # Add related_name for groups and user_permissions to avoid clashes with auth.User
    groups = models.ManyToManyField(
        Group,
        related_name="customuser_groups",  # Custom related_name to prevent clash
        blank=True
    )
    
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="customuser_permissions",  # Custom related_name to prevent clash
        blank=True
    )
