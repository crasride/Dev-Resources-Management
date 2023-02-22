from django.forms import ModelForm
from .models import Book, Author, Techno

# Define a form for the Book model
class BooksForm(ModelForm):
    # The Meta class is used to specify details of the model in the form
    class Meta:
        # Specify the model to work with
        model = Book
        # Specify the fields that will be available in the form
        fields = ['title', 'author', 'year', 'techno', 'language', 'image', 'pdf_link', 'description']

# Define a form for the Author model
class AuthorForm(ModelForm):
    # The Meta class is used to specify details of the model in the form
    class Meta:
        # Specify the model to work with
        model = Author
        # Specify the fields that will be available in the form
        fields = ['name']

# Define a form for the Techno model
class TechnoForm(ModelForm):
    # The Meta class is used to specify details of the model in the form
    class Meta:
        # Specify the model to work with
        model = Techno
        # Specify the fields that will be available in the form
        fields = ['name']
