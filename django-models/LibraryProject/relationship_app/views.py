from .models import Library  # Import the Library model
from django.shortcuts import render
from relationship_app.models import Book
from django.views.generic.detail import DetailView  # Correct import for DetailView
from relationship_app.models import Library
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse

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
