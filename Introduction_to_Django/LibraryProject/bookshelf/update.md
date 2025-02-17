from bookshelf.models import Book

# Fetch the book and update its title
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()

# Verifying update
print(Book.objects.get(id=book.id))

# Expected Output:
# Nineteen Eighty-Four by George Orwell (1949)
