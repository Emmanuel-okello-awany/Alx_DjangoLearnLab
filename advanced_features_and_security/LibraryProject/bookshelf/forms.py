from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date']

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if not title.isalnum():
            raise forms.ValidationError("Title must be alphanumeric.")
        return title

    def clean_author(self):
        author = self.cleaned_data.get('author')
        if not all(x.isalpha() or x.isspace() for x in author):
            raise forms.ValidationError("Author name must contain only letters and spaces.")
        return author

class ExampleForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

   
