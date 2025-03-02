from django.contrib import admin

# bookshelf/admin.py
from django.contrib import admin
from .models import Book

# Create a custom admin interface for the Book model
class BookAdmin(admin.ModelAdmin):
    # Display these fields in the list view
    list_display = ('title', 'author', 'publication_year')

    # Add filters in the admin interface
    list_filter = ('author', 'publication_year')

    # Enable search functionality on title and author fields
    search_fields = ('title', 'author')

# Register the Book model with the customized admin interface
admin.site.register(Book, BookAdmin)


# Register your models here.
