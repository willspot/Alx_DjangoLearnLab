from django.urls import path
from .views import list_books, LibraryDetailView  # Import the views here
from django.contrib.auth import views as auth_views
from relationship_app import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page for logged-in users

    # URL pattern for LoginView (customized to use your template)
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),

    # URL pattern for LogoutView (customized to use your template)
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),

    # URL pattern for Register (custom registration view)
    path('register/', register, name='register'),

    # URL pattern for the function-based view (FBV)
    path('books/', list_books, name='list_books'),

    # URL pattern for the class-based view (CBV)
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

     # Authentication URLs
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
]
