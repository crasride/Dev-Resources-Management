from django.urls import path
from . import views
from library import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

'''
   This code defines the URLs of the web application in Django, which are 
    accessible through the browser's address bar. Each URL is associated with a 
    view, which is a Python function that processes the request and returns a 
    response. In addition, paths are defined for the static and media files that
    are used in the application.
'''

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cookies_policy/', views.cookies_policy, name='cookies_policy'),
    path('contact/', views.contact, name='contact'),
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

