# Delete Operation

**Command**:
```python
from bookshelf.models import Book  # Import the Book model

# Delete the book
book.delete()

# Verify deletion by trying to retrieve the book again
try:
    book_deleted = Book.objects.get(title="Nineteen Eighty-Four")
except Book.DoesNotExist:
    print("The book has been deleted.")
