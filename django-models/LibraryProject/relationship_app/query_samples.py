from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    for book in books:
        print(book.title)

# List all books in a library
def books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    for book in books:
        print(book.title)

# Retrieve the librarian for a library
def librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = Librarian.objects.get(library=library)
    print(f"Librarian for {library_name}: {librarian.name}")

if __name__ == "__main__":
    # Example queries
    print("Books by Author 'J.K. Rowling':")
    books_by_author("J.K. Rowling")
    
    print("\nBooks in 'Central Library':")
    books_in_library("Central Library")
    
    print("\nLibrarian for 'Central Library':")
    librarian_for_library("Central Library")
