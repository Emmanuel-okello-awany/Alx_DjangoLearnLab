## **CRUD Operations for the Book Model**
This document details the commands used to perform CRUD (Create, Retrieve, Update, Delete) operations on the `Book` model using Django's ORM in the Django shell.

---

### **1. Create a Book Instance**
Run the following command in the Django shell to create a new book:
```python
from bookshelf.models import Book

# Create a new Book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# Verify creation
print(book)
```
**Expected Output:**
```python
<Book: 1984 by George Orwell (1949)>
```

---

### **2. Retrieve the Book Instance**
Retrieve the book instance from the database:
```python
# Retrieve the book we just created
book = Book.objects.get(title="1984")

# Display book details
print(f"Title: {book.title}, Author: {book.author}, Year: {book.publication_year}")
```
**Expected Output:**
```python
Title: 1984, Author: George Orwell, Year: 1949
```

---

### **3. Update the Book Title**
Update the title of the book from `"1984"` to `"Nineteen Eighty-Four"`:
```python
# Retrieve the book
book = Book.objects.get(title="1984")

# Update the title
book.title = "Nineteen Eighty-Four"
book.save()

# Verify update
updated_book = Book.objects.get(id=book.id)
print(f"Updated Title: {updated_book.title}")
```
**Expected Output:**
```python
Updated Title: Nineteen Eighty-Four
```

---

### **4. Delete the Book Instance**
Delete the book instance from the database:
```python
# Retrieve the book
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book
book.delete()

# Confirm deletion
books_remaining = Book.objects.all()
print(f"Remaining books: {list(books_remaining)}")
```
**Expected Output:**
```python
Remaining books: []
```

---

### **Summary**
| Operation  | Command Used |
|------------|-------------|
| **Create** | `Book.objects.create(title="1984", author="George Orwell", publication_year=1949)` |
| **Retrieve** | `Book.objects.get(title="1984")` |
| **Update** | `book.title = "Nineteen Eighty-Four"; book.save()` |
| **Delete** | `book.delete()` |

This document serves as a guide for performing CRUD operations on the `Book` model in Django.

---

### ✅ **Next Steps**
- Automate CRUD operations through Django views and templates.
- Use Django Admin to manage book entries.
- Implement a Django REST API for book management.

