from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet

# Initialize the router
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')  # Register the ViewSet


urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),  # Maps to the BookList view
    # Include all router-generated URL patterns
    path('', include(router.urls)),  # This automatically handles all CRUD routes for Book
]
