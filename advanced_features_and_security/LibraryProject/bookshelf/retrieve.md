## **Retrieve Book Instance**

To retrieve the book instance from the database, use the following command in the Django shell:

```python
from bookshelf.models import Book

# Retrieve the book we just created
book = Book.objects.get(title="1984")

# Display book details
print(f"Title: {book.title}, Author: {book.author}, Year: {book.publication_year}")

#output
#Title: 1984, Author: George Orwell, Year: 1949
