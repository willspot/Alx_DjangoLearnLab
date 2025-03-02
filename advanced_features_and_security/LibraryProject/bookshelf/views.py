from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Book

# View to list books, accessible only by users with the 'can_view' permission
@permission_required('library.can_view', raise_exception=True)
def view_books(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/view_books.html', {'books': books})

# View to create a new book, accessible only by users with 'can_create' permission
@permission_required('library.can_create', raise_exception=True)
def create_book(request):
    if request.method == "POST":
        # Logic to create book
        pass
    return render(request, 'bookshelf/create_book.html')

# View to edit a book, accessible only by users with 'can_edit' permission
@permission_required('library.can_edit', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        # Logic to edit book
        pass
    return render(request, 'bookshelf/edit_book.html', {'book': book})

# View to delete a book, accessible only by users with 'can_delete' permission
@permission_required('library.can_delete', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect('book_list')  # Redirect to the book list page
    return render(request, 'bookshelf/delete_book.html', {'book': book})

# Create your views here.
