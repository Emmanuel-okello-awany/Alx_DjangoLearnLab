from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Article
from .forms import ExampleForm

@permission_required('your_app.can_view', raise_exception=True)
def article_list(request):
    """ View articles (requires 'can_view' permission) """
    articles = Article.objects.all()
    return render(request, 'articles/list.html', {'articles': articles})

@permission_required('your_app.can_create', raise_exception=True)
def article_create(request):
    """ Create article (requires 'can_create' permission) """
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        Article.objects.create(title=title, content=content)
    return render(request, 'articles/create.html')

@permission_required('your_app.can_edit', raise_exception=True)
def article_edit(request, article_id):
    """ Edit article (requires 'can_edit' permission) """
    article = get_object_or_404(Article, id=article_id)
    if request.method == 'POST':
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.save()
    return render(request, 'articles/edit.html', {'article': article})

@permission_required('your_app.can_delete', raise_exception=True)
def article_delete(request, article_id):
    """ Delete article (requires 'can_delete' permission) """
    article = get_object_or_404(Article, id=article_id)
    article.delete()
    return render(request, 'articles/delete_success.html')


from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Book

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    # Logic to create a book
    pass

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    # Logic to edit the book
    pass

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    # Redirect or render response

def example_form_view(request):
    if request.method == "POST":
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Process the valid data (e.g., save it, send an email, etc.)
            return render(request, "bookshelf/example_success.html", {"form": form})
    else:
        form = ExampleForm()

    return render(request, "bookshelf/form_example.html", {"form": form})