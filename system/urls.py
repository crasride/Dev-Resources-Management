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
    path('favorites/<int:book_id>/', views.favorites, name='favorites'),
    path('favorites_list/', views.favorites_list, name='favorites_list'),
    path('book_detail_favorites/<int:book_id>/', views.book_detail_favorites, name='book_detail_favorites'),
    path('create_books/', views.create_books, name='create_books'),
    path('delete_books/<int:id>/', views.delete_books, name='delete_books'),
    path('search_books/<int:id>/', views.search_books, name='search_books'),
    path('search_books/', views.search_books, name='search_books'),
    path('book_detail/<int:book_id>/', views.book_detail, name='book_detail'),
    path('search_books_online/', views.search_books_online, name='search_books_online'),
    path('create_cheatsheet/', views.create_cheatsheet, name='create_cheatsheet'),
    path('delete_cheats/<int:id>/', views.delete_cheats, name='delete_cheats'),
    path('cheats/', views.cheats, name='cheats'),
    path('techno_form/', views.techno_form, name='techno_form'),
    path('author_form/', views.author_form, name='author_form'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
 + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
  
