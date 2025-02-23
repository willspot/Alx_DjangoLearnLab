from relationship_app.models import Author, Book, Library, Librarian

# Query 1: Retrieve all books by a specific author
def get_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = author.books.all()  # Using the related_name from ForeignKey
    for book in books:
        print(book.title)

# Query 2: List all books in a specific library
def get_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()  # Using the related_name from ManyToManyField
    for book in books:
        print(book.title)

# Query 3: Retrieve the librarian for a specific library
def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = library.librarian  # Using the related_name from OneToOneField
    print(f"The librarian for {library_name} is {librarian.name}")

# Example usage
if __name__ == '__main__':
    print("Books by Author 'J.K. Rowling':")
    get_books_by_author('J.K. Rowling')

    print("\nBooks in Library 'City Library':")
    get_books_in_library('City Library')

    print("\nLibrarian for 'City Library':")
    get_librarian_for_library('City Library')
