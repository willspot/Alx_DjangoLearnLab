from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('', views.PostListView.as_view(), name='post-list'),  # List all posts
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),  # Create new post
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),  # View post details
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),  # Edit existing post
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),  # Delete existing post
    path('', views.PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', views.post_detail, name='post-detail'),
    path('post/<int:pk>/comments/new/', views.post_detail, name='post-comment'),
    path('comments/<int:pk>/edit/', views.edit_comment, name='edit-comment'),
    path('comments/<int:pk>/delete/', views.delete_comment, name='delete-comment'),
     path('', views.PostListView.as_view(), name='post-list'),
    path('posts/<int:pk>/', views.post_detail, name='post-detail'),
    path('posts/<int:post_pk>/comments/new/', views.CommentCreateView.as_view(), name='comment-create'),
    path('comment/<int:pk>/update/', views.CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment-delete'),
]
