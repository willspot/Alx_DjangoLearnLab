from django.shortcuts import render
from relationship_app.models import Book
from django.views.generic import DetailView
from relationship_app.models import Library

# Function-based view to list all books
def list_books(request):
    # Fetch all books from the database
    books = Book.objects.all()
    
    # Render the list_books template and pass the books context
    return render(request, 'list_books.html', {'books': books})

# Class-based view to show details of a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'  # Specify the template for rendering the library detail page
    context_object_name = 'library'  # Context name used in the template