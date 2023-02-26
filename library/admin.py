from django.contrib import admin
from .models import Book, Techno, Language, Author, CheatSheet, Favorites

class BookAdmin(admin.ModelAdmin):
    readonly_fields = ("created", )

# Register your models here.
admin.site.register(Book, BookAdmin)
admin.site.register(Techno)
admin.site.register(Language)
admin.site.register(Author)
admin.site.register(CheatSheet)
admin.site.register(Favorites)
