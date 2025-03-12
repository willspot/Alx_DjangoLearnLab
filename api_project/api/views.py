from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Book  # Assuming your Book model is in the same app
from .serializers import BookSerializer

# Create your views here.
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()  # Retrieves all books from the database
    serializer_class = BookSerializer  # Specifies the serializer to use

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()  # All books will be retrieved from the database
    serializer_class = BookSerializer  # The serializer to use for these operations
    permission_classes = [IsAuthenticated]  # Only authenticated users can access these views