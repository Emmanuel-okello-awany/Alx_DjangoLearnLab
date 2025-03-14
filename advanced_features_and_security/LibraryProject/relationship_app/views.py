from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required, user_passes_test
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Book, Library, UserProfile
from django.views.generic.detail import DetailView
from django.contrib.auth.models import Group, Permission
from django.contrib.auth.decorators import permission_required

# List books
@permission_required('relationship_app.can_view_book', raise_exception=True)
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})

# Library detail view
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

# Home page view
def home(request):
    return render(request, "relationship_app/home.html", {"message": "Welcome to the Library System!"})

# User Login View
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("list_books")
    else:
        form = AuthenticationForm()
    return render(request, "relationship_app/login.html", {"form": form})

# User Logout View
def logout_view(request):
    logout(request)
    return redirect("home")

# User Registration View
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Get role from form or set default
            role = request.POST.get('role', 'Member')

            # Create or get existing user profile
            user_profile, created = UserProfile.objects.get_or_create(user=user)
            user_profile.role = role  # Assign role
            user_profile.save()  # Save the profile

            # Assign permissions based on role
            if role == 'Admin':
                permissions = [
                    "can_add_book",
                    "can_change_book",
                    "can_delete_book"
                ]
            elif role == 'Librarian':
                permissions = ["can_change_book"]
            else:
                permissions = []  # Members get no special permissions

            # Assign permissions to user
            for perm in permissions:
                permission = Permission.objects.get(codename=perm)
                user.user_permissions.add(permission)

            # Redirect to login page after successful registration
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'relationship_app/register.html', {'form': form})
# Admin check function and view
def is_admin(user):
    return user.is_authenticated and user.userprofile.role == "Admin"
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, "relationship_app/admin_view.html", {"message": "Welcome, Admin!"})

# Librarian check function and view
def is_librarian(user):
    return user.is_authenticated and user.userprofile.role == "Librarian"

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, "relationship_app/librarian_view.html", {"message": "Welcome, Librarian!"})

# Member check function and view
def is_member(user):
    return user.is_authenticated and user.userprofile.role == "Member"

@user_passes_test(is_member)
def member_view(request):
    return render(request, "relationship_app/member_view.html", {"message": "Welcome, Member!"})

# Add book view with permission check
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == "POST":
        # Handle form submission for adding a book
        pass
    return render(request, "relationship_app/add_book.html")

# Edit book view with permission check
@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        # Handle form submission for editing the book
        pass
    return render(request, "relationship_app/edit_book.html", {"book": book})

# Delete book view with permission check
@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect("list_books")
    return render(request, "relationship_app/delete_book.html", {"book": book})



