from django.shortcuts import render
from rest_framework import generics
from .models import Book  # Assuming your Book model is in the same app
from .serializers import BookSerializer

# Create your views here.
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()  # Retrieves all books from the database
    serializer_class = BookSerializer  # Specifies the serializer to use