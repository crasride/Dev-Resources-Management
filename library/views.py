from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import BooksForm, AuthorForm,TechnoForm
from .models import Book, Author, Techno
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


# Definition of functions for interaction with the books table.(section)

@login_required # Route Protection
def books(request):
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
    try:
        book = get_object_or_404(Book, id=id, user=request.user)
    except Book.DoesNotExist:
        messages.error(request, 'Error: The book does not exist')
        return redirect('books')
    
    if book.user == request.user:
        book.delete()
        messages.success(request, 'The book has been successfully removed!', extra_tags='success')
    else:
        messages.error(request, 'You do not have permission to delete this book', extra_tags='danger')
    
    return redirect('books')

@login_required # Route Protection
def search_books(request):
    if request.method == 'GET':
        query = request.GET.get('q')

        if query:
            books = Book.objects.filter(techno__name__icontains=query) | Book.objects.filter(author__name__icontains=query)
        else:
            books = Book.objects.all()

        return render(request, 'search_books.html', {'books': books, 'query': query})

@login_required 
def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'book_detail.html', {'book': book})


# Definition of functions for interaction with the author table.(section)

@login_required # Route Protection
def author(request):
    list = Author.objects.all()
    # list = Author.objects.filter(user=request.user)
    return render(request, 'author.html', {"list": list})

@login_required # Route Protection
def create_author(request):
    if request.method == 'GET':
        return render(request, 'author.html', {'form': AuthorForm})
    else:
        form = AuthorForm(request.POST or None)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            # Verificar si el autor ya existe en la base de datos
            if Author.objects.filter(name=name).exists():
                return render(request, 'author.html', {
                    'form': form,
                    'error': 'An author with this name already exists.'
                })
            else:
                new_author = form.save(commit=False)
                new_author.user = request.user
                new_author.save()
                return redirect('create_books')
        else:
            return render(request, 'author.html', {
                'form': form,
                'error': 'Please provide valid data.'
            })

# Definition of functions for interaction with the techno table.(section)
def create_techno(request):
    if request.method == 'GET':
        return render(request, 'create_techno.html', {'form': TechnoForm})
    else:
        form = TechnoForm(request.POST or None)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            # Verificar si el autor ya existe en la base de datos
            if Techno.objects.filter(name=name).exists():
                return render(request, 'create_techno.html', {
                    'form': form,
                    'error': 'An tecnho with this name already exists.'
                })
            else:
                new_techno = form.save(commit=False)
                new_techno.user = request.user
                new_techno.save()
                return redirect('create_books')
        else:
            return render(request, 'create_techno.html', {
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

