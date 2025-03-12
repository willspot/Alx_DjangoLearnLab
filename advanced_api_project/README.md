# API Documentation for advanced_api_project

## Endpoints

### `GET /books/`
- Retrieves a list of all books.
- **Permissions**: No authentication required.

### `POST /books/`
- Creates a new book.
- **Permissions**: No authentication required.

### `GET /books/<int:pk>/`
- Retrieves the details of a single book by `id`.
- **Permissions**: Authenticated users only.

### `PUT /books/<int:pk>/`
- Updates the details of a book.
- **Permissions**: Authenticated users only.

### `DELETE /books/<int:pk>/`
- Deletes a book.
- **Permissions**: Authenticated users only.

## Permissions
- `BookListView` allows open access for reading and creating books.
- `BookDetailView` restricts updates and deletions to authenticated users only.

## Testing
- Use tools like Postman or cURL to test these endpoints.

# Book API Endpoints

## Filtering
- **title**: `/books/?title=Harry Potter`
- **author__name**: `/books/?author__name=J.K. Rowling`
- **publication_year**: `/books/?publication_year=1997`

## Searching
- **search**: `/books/?search=Harry`
  - Search by title or author name.

## Ordering
- **ordering**: `/books/?ordering=publication_year`
  - Order by title or publication year (ascending/descending).
  - Example: `/books/?ordering=-publication_year` (descending order).

## Testing the API

To test the API endpoints, you can run the following command:

