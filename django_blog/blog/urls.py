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
    path('posts/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),  # Edit existing post
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),  # Delete existing post
]
