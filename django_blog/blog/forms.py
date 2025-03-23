from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post, Comment, Tag  # Make sure Tag is imported


# User Registration Form
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Required. Please enter a valid email address.")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered. Please use a different one.")
        return email


# Post Form - Create & Update with Tags
class PostForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter post title'}),
        max_length=255,
        required=True
    )
    content = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your content here...'}),
        required=True
    )
    tags = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter tags separated by commas'}),
        required=False
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
            # Handling tags input - splitting by commas, stripping whitespace, and adding tags
            tags_input = self.cleaned_data['tags']
            tag_names = [name.strip() for name in tags_input.split(',') if name.strip()]
            for tag_name in tag_names:
                tag, created = Tag.objects.get_or_create(name=tag_name)
                instance.tags.add(tag)
        return instance


# Comment Form - Create & Update
class CommentForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your comment here...'}),
        required=True
    )

    class Meta:
        model = Comment
        fields = ['content']


# Search Form
class SearchForm(forms.Form):
    query = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Search by title, content, or tags...'}),
        required=True
    )
