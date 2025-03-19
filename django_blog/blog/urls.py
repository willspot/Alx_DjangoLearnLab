from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('', views.PostListView.as_view(), name='post-list'),  # List all posts
    path('posts/new/', views.PostCreateView.as_view(), name='post-create'),  # Create new post
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),  # View post details
    path('posts/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post-edit'),  # Edit existing post
    path('posts/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),  # Delete existing post
]
