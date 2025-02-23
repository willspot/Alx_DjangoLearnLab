from .models import Library  # Import the Library model
from django.shortcuts import render
from relationship_app.models import Book
from django.views.generic.detail import DetailView  # Correct import for DetailView
from relationship_app.models import Library
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

# Registration view to allow users to register
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login after registration
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# Login view (Django built-in view)
class CustomLoginView(LoginView):
    template_name = 'relationship_app/login.html'

# Logout view (Django built-in view)
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