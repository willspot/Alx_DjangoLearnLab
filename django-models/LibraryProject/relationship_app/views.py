from .models import Library  # Import the Library model
from django.shortcuts import render
from relationship_app.models import Book
from django.views.generic.detail import DetailView  # Correct import for DetailView
from relationship_app.models import Library
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required
from .models import Book

# View to add a new book (requires 'can_add_book' permission)
@permission_required('relationship_app.can_add_book')
def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author_id = request.POST.get('author')
        publication_year = request.POST.get('publication_year')
        
        # Add the book to the database
        new_book = Book.objects.create(
            title=title, 
            author_id=author_id, 
            publication_year=publication_year
        )
        return redirect('book_list')  # Redirect to the list of books

    return render(request, 'add_book.html')


# View to edit an existing book (requires 'can_change_book' permission)
@permission_required('relationship_app.can_change_book')
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author_id = request.POST.get('author')
        book.publication_year = request.POST.get('publication_year')
        book.save()
        return redirect('book_list')  # Redirect to the list of books

    return render(request, 'edit_book.html', {'book': book})


# View to delete a book (requires 'can_delete_book' permission)
@permission_required('relationship_app.can_delete_book')
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')  # Redirect to the list of books

    return render(request, 'delete_book.html', {'book': book})


# Helper function to check if the user has the 'Admin' role
def is_admin(user):
    return user.userprofile.role == 'Admin'

# Helper function to check if the user has the 'Librarian' role
def is_librarian(user):
    return user.userprofile.role == 'Librarian'

# Helper function to check if the user has the 'Member' role
def is_member(user):
    return user.userprofile.role == 'Member'

# Admin view (accessible only by 'Admin' users)
@user_passes_test(is_admin)
def admin_view(request):
    return HttpResponse('Welcome to the Admin Dashboard!')

# Librarian view (accessible only by 'Librarian' users)
@user_passes_test(is_librarian)
def librarian_view(request):
    return HttpResponse('Welcome to the Librarian Dashboard!')

# Member view (accessible only by 'Member' users)
@user_passes_test(is_member)
def member_view(request):
    return HttpResponse('Welcome to the Member Dashboard!')


# Registration view to allow users to register and log them in immediately
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # Save the new user and log them in
            user = form.save()
            login(request, user)  # Automatically log in the user after registration
            return redirect('home')  # Redirect to a homepage or dashboard (you can change this URL)
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# Custom login view (Django built-in view)
class CustomLoginView(LoginView):
    template_name = 'relationship_app/login.html'

# Custom logout view (Django built-in view)
class CustomLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'

# Function-based view to list all books
def list_books(request):
    # Fetch all books from the database
    books = Book.objects.all()
    
    # Render the list_books template and pass the books context
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view to show details of a specific library
class LibraryDetailView(DetailView):
    model = Library  # Define the model to use for this view
    template_name = 'relationship_app/library_detail.html'  # Specify the template for rendering the library detail page
    context_object_name = 'library'  # Context name used in the template

def home(request):
    return render(request, 'relationship_app/home.html')  # Create a template for the home page
