from django.urls import path
from .views import list_books, LibraryDetailView  # Import the views here
from django.contrib.auth import views as auth_views

urlpatterns = [
    # URL pattern for the function-based view (FBV)
    path('books/', list_books, name='list_books'),

    # URL pattern for the class-based view (CBV)
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

     # Authentication URLs
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
]
