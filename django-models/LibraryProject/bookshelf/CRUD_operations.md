# CRUD Operations Documentation

## Create Operation
**Command**:
```python
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(book)

book_retrieved = Book.objects.get(title="1984")
print(book_retrieved)

book.title = "Nineteen Eighty-Four"
book.save()
print(book)

book.delete()

try:
    book_deleted = Book.objects.get(title="Nineteen Eighty-Four")
except Book.DoesNotExist:
    print("The book has been deleted.")


