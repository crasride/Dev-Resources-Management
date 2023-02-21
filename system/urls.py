"""system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from library import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('signup/', views.signup, name='signup'),
    path('books/', views.books, name='books'),
    path('create_books/', views.create_books, name='create_books'),
    path('delete_books/<int:id>/', views.delete_books, name='delete_books'),
    path('search_books/<int:id>/', views.search_books, name='search_books'),
    path('search_books/', views.search_books, name='search_books'),
    path('book_detail/<int:book_id>/', views.book_detail, name='book_detail'),
    path('search_books_online/', views.search_books_online, name='search_books_online'),
    path('author/', views.author, name='author'),
    path('create_author/', views.create_author, name='create_author'),
    path('create_techno/', views.create_techno, name='create_techno'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
 + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
  
