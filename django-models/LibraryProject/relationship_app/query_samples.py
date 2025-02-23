from relationship_app.models import Author, Book, Library, Librarian

# Query 1: Retrieve all books by a specific author
def get_books_by_author(author_name):
    # Fetch the author by name
    author = Author.objects.get(name=author_name)
    
    # Query all books written by this author
    books = Book.objects.filter(author=author)  # Use filter to get books by the author
    
    # Print the titles of the books
    for book in books:
        print(book.title)

# Query 2: List all books in a specific library
def get_books_in_library(library_name):
    # Fetch the library by name
    library = Library.objects.get(name=library_name)
    
    # Query all books in this library (ManyToMany relationship)
    books = library.books.all()  # Use the related_name 'books' for ManyToManyField
    
    # Print the titles of the books
    for book in books:
        print(book.title)

# Query 3: Retrieve the librarian for a specific library
def get_librarian_for_library(library_name):
    # Fetch the library by name
    library = Library.objects.get(name=library_name)
    
    # Retrieve the librarian for this library (OneToOneField)
    librarian = Librarian.objects.get(library=library)  # Correct query using OneToOneField
    
    # Print the librarian's name
    print(f"The librarian for {library_name} is {librarian.name}")

# Example usage
if __name__ == '__main__':
    print("Books by Author 'J.K. Rowling':")
    get_books_by_author('J.K. Rowling')

    print("\nBooks in Library 'City Library':")
    get_books_in_library('City Library')

    print("\nLibrarian for 'City Library':")
    get_librarian_for_library('City Library')
