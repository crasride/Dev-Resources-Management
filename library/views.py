from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
# the browser knows that we are authenticated
from django.contrib.auth import login, logout, authenticate
# from django.http import HttpResponse
from django.db import IntegrityError

# Create your views here.


def home(request):
    return render(request, 'home.html')


def signup(request):

    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.
                                                POST['password1'])
                user.save()
                # create the cookie
                login(request, user)
                return redirect('listbooks')
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


def listbooks(request):
    return render(request, 'listbooks.html')


def signout(request):
    logout(request)
    return redirect('home')


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        # check data by console
        # print(request.POST)
        user = authenticate(
            request, username=request.POST['username'], password=request.POST
            ['password'])
        # if the username is not valid it gives an error
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Username or password is incorrect'
            })
        else:
            login(request, user)
            return redirect('listbooks')
