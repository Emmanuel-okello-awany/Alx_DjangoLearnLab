from relationship_app.models import Book, Author, Library

# Create Authors
author1 = Author.objects.create(name="J.K. Rowling")
author2 = Author.objects.create(name="George Orwell")
author3 = Author.objects.create(name="Chinua Achebe")

# Create Libraries
library1 = Library.objects.create(name="Central Library")
library2 = Library.objects.create(name="Community Library")

# Create Books
book1 = Book.objects.create(title="Harry Potter", author=author1)
book2 = Book.objects.create(title="1984", author=author2)
book3 = Book.objects.create(title="Animal Farm", author=author2)
book4 = Book.objects.create(title="Things Fall Apart", author=author3)

# Assign Books to Libraries
library1.books.add(book1, book2)
library2.books.add(book3, book4)

print("Books and libraries added successfully!")
