from rest_framework import serializers
from .models import Book  # Assuming you have a Book model

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book  # Your Book model
        fields = '__all__'  # This will include all fields in the Book model