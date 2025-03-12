from django.shortcuts import render
from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListCreateAPIView):
    """
    Handles GET and POST requests for Books.
    - GET: Returns a list of all books.
    - POST: Allows the creation of a new book.
    Permission: Open to all users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = []  # Open to unauthenticated users (read-only access)
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['title', 'publication_year']  # Allow ordering by title or year
    ordering = ['title']  # Default ordering by title

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

