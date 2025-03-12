from django.shortcuts import render
from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListCreateAPIView):
    """
    Handles GET and POST requests for Books.
    - GET: Retrieves a list of books with filtering, searching, and ordering capabilities.
    - POST: Allows the creation of a new book.

    Filtering:
    - title: Filter books by title.
    - author__name: Filter books by author name.
    - publication_year: Filter books by publication year.

    Searching:
    - title: Search books by title.
    - author__name: Search books by author name.

    Ordering:
    - title: Order books by title (ascending or descending).
    - publication_year: Order books by publication year (ascending or descending).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_fields = ['title', 'author__name', 'publication_year']  # Allows filtering by title, author name, and publication year
    ordering_fields = ['title', 'publication_year']  # Users can order by title or publication year
    permission_classes = []  # Open to unauthenticated users (read-only access)
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['title', 'publication_year']  # Allow ordering by title or year
    ordering = ['title']  # Default ordering by title
    search_fields = ['title', 'author__name']  # Allow searching by title or author name

    def perform_create(self, serializer):
        # Optionally, add custom logic here (e.g., assign author based on request)
        serializer.save()

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Handles GET (retrieve single book), PUT/PATCH (update a book), and DELETE requests.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Restricted to authenticated users

