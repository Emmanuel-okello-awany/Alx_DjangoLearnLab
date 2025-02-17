from bookshelf.models import Book

# Retrieving all books
books = Book.objects.all()
for book in books:
    print(book)

# Expected Output:
# 1984 by George Orwell (1949)
