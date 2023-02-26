from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import BooksForm, AuthorForm, TechnoForm, CheatsheetForm
from .models import Book, Author, Techno, CheatSheet, Favorites
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import requests


# Create your views here.


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

# Definition of functions for interaction with the openlibrary-client (section)

@login_required
def search_books_online(request):
    '''
    Management an online search through the API Open Library and I show the
     results, if the HTTP search is successful, the JSON answer is analyzed and
     the relevant data of the answer are extracted and if it does not give me
    an error.
    '''
    query = request.GET.get('q')
    if query:
        url = f'http://openlibrary.org/search.json?q={query}&limit=20'
        response = requests.get(url)
        if response.status_code == 200:
            books = response.json().get('docs', [])
            # print(books)
            return render(request, 'search_books_online.html', {'books': books, 'query': query})
        else:
            error_message = f'An error occurred while searching for books: {response.status_code}'
            return render(request, 'search_books_online.html', {'error': error_message, 'query': query})
    else:
        return render(request, 'search_books_online.html')

# Definition of functions for interaction with the favorites table.(section)
@login_required # Route Protection
def favorites(request, book_id):
    '''
     It is the addition of a book to a user's favorites and verify if the book
      is already on the user's favorites list before adding it.If the book
      already exists in favorites, it gives me an error and if it adds it
      to me and gives me an OK message.
    '''
    book = get_object_or_404(Book, id=book_id)

    # Check if the book is already in the user's favorites
    if Favorites.objects.filter(user=request.user, books=book).exists():
        messages.error(request, "This book is already in your favorites.")
        return redirect('books')

    # Create a new favorite book object
    favorite_book = Favorites(user=request.user)
    favorite_book.save()
    favorite_book.books.add(book)

    messages.success(request, "The book has been added to your favorites.")
    return redirect('books')

@login_required # Route Protection
def favorites_list(request):
    # Get all Favorites objects for the current user
    favorites = Favorites.objects.filter(user=request.user).select_related('user')
    # Create a context dictionary containing the list of Favorites objects
    context = {
        'favorites': favorites
    }
    return render(request, 'favorites_list.html', context)

@login_required # Route Protection
def book_detail_favorites(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'book_detail_favorites.html', {'book': book})

# Definition of functions for interaction with the books table.(section)

@login_required # Route Protection
def books(request):
    '''
     Returns a list of books
    '''
    list = Book.objects.all()
    # list = Book.objects.filter(user=request.user)
    return render(request, 'books.html', {"list": list})

@login_required # Route Protection
def create_books(request):
    # If request method is GET, display create_books.html page with the BooksForm
    if request.method == 'GET':
        return render(request, 'create_books.html', {'form': BooksForm})
    else:
        try:
            # If request method is POST, validate the BooksForm data
            form = BooksForm(request.POST or None, request.FILES or None)
            new_book = form.save(commit=False)
            # Assign the current user to the new_book object
            new_book.user = request.user
            # Save the new book object to the database
            new_book.save()
            # Redirect to the books page
            return redirect('books')
        except ValueError:
            # If there is a value error, display the create_books.html page with the BooksForm and an error message
            return render(request, 'create_books.html', {
                'form': BooksForm,
                'error': 'Please provide valid data'
            })


@login_required # Route Protection
def delete_books(request, id):
    '''
      Delete a book from the database
    '''
    try:
        # Retrieve the book object to delete
        book = get_object_or_404(Book, id=id, user=request.user)
    except Book.DoesNotExist:
        # The book doesn't exist, display an error message and redirect
        messages.error(request, 'Error: The book does not exist')
        return redirect('books')
     # The user is authorized to delete the book
    if book.user == request.user:
        book.delete()
        messages.success(
            request, 'The book has been successfully removed!', extra_tags='success')
    else:
        # The user is not authorizedn error message
        messages.error(
            request, 'You do not have permission to delete this book', extra_tags='danger')

    return redirect('books')


@login_required # Route Protection
def search_books(request):
    '''
     Search for books by Author or Technology
    '''
      # Check the method is GET
    if request.method == 'GET':
        query = request.GET.get('q')

        if query:
             # Filter the books by author or technology
            books = Book.objects.filter(techno__name__icontains=query) | Book.objects.filter(
                author__name__icontains=query)
        else:
            # Return all books
            books = Book.objects.all()

        return render(request, 'search_books.html', {'books': books, 'query': query})


@login_required # Route Protection
def book_detail(request, book_id):
    '''
      Book details
    '''
     # Get the book with the given ID , or return  404 error if it doesn't exist
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'book_detail.html', {'book': book})


# Definition of functions for interaction with the author table.(section)
@login_required # Route Protection
def author_form(request):
    '''
     I verify if the HTTP method is get and then create an object through an
      HTML form if there is an object with the same name or already exist in
      the database, an error message is shown and if the data sent in the Form,
      before saving them in the database.
    '''
    if request.method == 'GET':
        return render(request, 'author_form.html', {'form': AuthorForm()})
    else:
        form = AuthorForm(request.POST or None)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            if Author.objects.filter(name=name).exists():
                return render(request, 'author_form.html', {
                    'form': form,
                    'error': 'A techno with this name already exists.'
                })
            else:
                new_techno = form.save(commit=False)
                new_techno.user = request.user
                new_techno.save()
                return render(request, 'author_form.html', {'success': True})
        else:
            return render(request, 'author_form.html', {
                'form': form,
                'error': 'Please provide valid data.'
            })

# Definition of functions for interaction with the cheatsheet table.(section)
@login_required # Route Protection
def create_cheatsheet(request):
    # If request method is GET, display create_cheatsheet.html page with the CheatsheetForm
    if request.method == 'GET':
        return render(request, 'create_cheatsheet.html', {'form': CheatsheetForm})
    else:
        try:
            # If request method is POST, validate the CheatsheetForm data
            form = CheatsheetForm(request.POST or None, request.FILES or None)
            new_cheatsheet = form.save(commit=False)
            # Assign the current user to the new_cheatsheet object
            new_cheatsheet.user = request.user
            print (new_cheatsheet)
            # Save the new cheatsheet object to the database
            new_cheatsheet.save()
            # Redirect to the cheatsheets page
            return redirect('create_cheatsheet')
        except ValueError:
            # If there is a value error, display the create_cheatsheet.html page with the CheatsheetForm and an error message
            return render(request, 'create_cheatsheet.html', {
                'form': CheatsheetForm,
                'error': 'Please provide valid data'
            })

@login_required # Route Protection
def cheats(request):
    list = CheatSheet.objects.all()
    # list = cheats.objects.filter(user=request.user)
    return render(request, 'cheats.html', {"list": list})

@login_required  # Route Protection
def delete_cheats(request, id):
    '''
      Delete a cheatsheet from the database
    '''
    try:
        cheats = get_object_or_404(CheatSheet, id=id, user=request.user)
    except CheatSheet.DoesNotExist:
        messages.error(request, 'Error: The CheatSheet does not exist')
        return redirect('cheats')

    if cheats.user == request.user:
        cheats.delete()
        messages.success(
            request, 'The CheatSheet has been successfully removed!', extra_tags='success')
    else:
        messages.error(
            request, 'You do not have permission to delete this CheatSheet', extra_tags='danger')

    return redirect('cheats')

# Definition of functions for interaction with the create techno table.(section)
@login_required # Route Protection
def techno_form(request):
    '''
     I verify if the HTTP method is get and then create an object through an
      HTML form if there is an object with the same name or already exist in
      the database, an error message is shown and if the data sent in the Form,
      before saving them in the database.
    '''
    if request.method == 'GET':
        return render(request, 'techno_form.html', {'form': TechnoForm()})
    else:
        form = TechnoForm(request.POST or None)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            if Techno.objects.filter(name=name).exists():
                return render(request, 'techno_form.html', {
                    'form': form,
                    'error': 'A techno with this name already exists.'
                })
            else:
                new_techno = form.save(commit=False)
                new_techno.user = request.user
                new_techno.save()
                return render(request, 'techno_form.html', {'success': True})
        else:
            return render(request, 'techno_form.html', {
                'form': form,
                'error': 'Please provide valid data.'
            })

# User authentication and creation interaction with the users table.(section)

def signup(request):
    '''
    GET, displays the page of a user registration form.
    If the username already exists, an error message is output. 
    If the passwords do not match, an error message is output and if created 
    successfully, the user is logged in and redirected to the home page.
    '''

    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm,
        })
    else:
        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.
                                                POST['password1'], email=request.POST['email'])
                user.save()
                # create the cookie
                login(request, user)
                return redirect('books')
                # return HttpResponse('User created successfully')
            except IntegrityError:
                # return HttpResponse('User name already exists')
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'User already exits'
                })

        return render(request, 'signup.html', {
            'form': UserCreationForm,
            'error': 'Password do not match'
        })

@login_required # Route Protection
def signout(request):
    '''
    When the session is closed, it takes a request object as an argument and 
    clears the session data with the associated user. And when the session is
    cleared, it redirects to the home page.
    '''
    logout(request)
    return redirect('home')

def signin(request):
    '''
    This function checks the login credentials of the user, if they are valid
     it logs in and if not it shows an error message.
    '''

    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST
            ['password'])
        # check data by console
        # print(request.POST)
        # if the username is not valid it gives an error
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Username or password is incorrect'
            })
        else:
            login(request, user)
            return redirect('books')
'''
class AddTechnoView(View):
    def post(self, request):
        form = TechnoForm(request.POST)
        if form.is_valid():
            techno_name = form.cleaned_data['name']
            techno = Techno.objects.create(name=techno_name)
            data = {'id': techno.pk, 'text': techno_name}
            return JsonResponse({'success': True, 'data': data})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
'''
