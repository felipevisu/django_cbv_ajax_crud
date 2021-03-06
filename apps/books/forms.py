from django import forms

from .models import Book

class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ['title', 'author', 'pages', 'book_type']
        widgets = {
            'book_type': forms.RadioSelect(),
        }