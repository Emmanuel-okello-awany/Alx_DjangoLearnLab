from bookshelf.models import Book

# Deleting the book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Verifying deletion
books = Book.objects.all()
print(books)

# Expected Output:
# <QuerySet []> (empty queryset, meaning no books exist)
