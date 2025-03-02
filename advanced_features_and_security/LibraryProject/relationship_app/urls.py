from django.urls import path
from .views import list_books, LibraryDetailView  # Import the views here
from django.contrib.auth import views as auth_views
from relationship_app import views
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('book/add/', views.add_book, name='add_book'),
    path('book/edit/<int:book_id>/', views.edit_book, name='edit_book'),
    path('book/delete/<int:book_id>/', views.delete_book, name='delete_book'),

    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),

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
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
