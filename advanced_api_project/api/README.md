# Advanced API Project

## Overview

This project is a Django REST Framework (DRF) API that provides CRUD operations for a `Book` model. It includes features such as filtering, searching, and ordering to enhance usability.

## Features

- **CRUD Operations**: Create, Read, Update, Delete books.
- **Authentication**: Some endpoints require authentication.
- **Filtering**: Filter books by title, author, and publication year.
- **Searching**: Search books by title and author.
- **Ordering**: Order books by title and publication year.

## API Endpoints

### 1. Book Endpoints

| Method | Endpoint           | Description                                                        | Authentication |
| ------ | ------------------ | ------------------------------------------------------------------ | -------------- |
| GET    | `/books/`          | Retrieve a list of books (supports filtering, searching, ordering) | No             |
| GET    | `/books/<int:pk>/` | Retrieve a single book by ID                                       | No             |
| POST   | `/books/`          | Create a new book entry                                            | Yes            |
| PUT    | `/books/<int:pk>/` | Update an existing book                                            | Yes            |
| DELETE | `/books/<int:pk>/` | Delete a book entry                                                | Yes            |

## Authentication Requirements

- **Authentication Method**: Token-based authentication.
- Users must be logged in to create, update, or delete books.
- Unauthenticated users can only retrieve books.

## Setup Instructions

### 1. Clone the Repository

```sh
git clone https://github.com/your-username/Alx_DjangoLearnLab.git
cd advanced-api-project
```

### 2. Create a Virtual Environment

```sh
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install Dependencies

```sh
pip install -r requirements.txt
```

### 4. Apply Migrations

```sh
python manage.py migrate
```

### 5. Create a Superuser

```sh
python manage.py createsuperuser
```

### 6. Run the Server

```sh
python manage.py runserver
```

## Testing Instructions

- Use **Postman** or **cURL** to test API endpoints.
- Example requests:

### Retrieve Books (GET)

```sh
curl -X GET http://127.0.0.1:8000/books/
```

### Create a Book (POST)

```sh
curl -X POST http://127.0.0.1:8000/books/ -H "Authorization: Token YOUR_TOKEN" -H "Content-Type: application/json" -d '{"title": "New Book", "author": "John Doe", "publication_year": 2023}'
```

### Update a Book (PUT)

```sh
curl -X PUT http://127.0.0.1:8000/books/1/ -H "Authorization: Token YOUR_TOKEN" -H "Content-Type: application/json" -d '{"title": "Updated Book"}'
```

### Delete a Book (DELETE)

```sh
curl -X DELETE http://127.0.0.1:8000/books/1/ -H "Authorization: Token YOUR_TOKEN"
```

## Additional Notes

- Ensure `DjangoFilterBackend`, `SearchFilter`, and `OrderingFilter` are enabled in `settings.py`.
- API tokens can be obtained after logging in via `/api/token/`.

---

### Author

**emmanuel awany**

