# Delete Operation

**Command**:
```python
book.delete()

try:
    book_deleted = Book.objects.get(title="Nineteen Eighty-Four")
except Book.DoesNotExist:
    print("The book has been deleted.")

