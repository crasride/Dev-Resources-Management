from django.forms import ModelForm
from .models import Book, Author, Techno


class BooksForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'year', 'techno',
                  'language', 'image', 'pdf_link', 'description']

class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['name']

class TechnoForm(ModelForm):
    class Meta:
        model = Techno
        fields = ['name']
