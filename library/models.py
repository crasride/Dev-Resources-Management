from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Techno(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Language(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, verbose_name='Author')

    def __str__(self):
        return self.name
    
class CheatSheet(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, verbose_name='Title')
    techno = models.ForeignKey(Techno, on_delete=models.RESTRICT, verbose_name='Techno')
    link_imagen = models.ImageField(upload_to='media/cheat_sheets/images/', verbose_name='Image', null=True, blank=True)
    pdf_link = models.FileField(upload_to='media/cheat_sheets/pdf/', verbose_name='Pdf', default='', blank=True)
    description = models.TextField(verbose_name='Description', blank=True)
    user = models.ForeignKey(User, on_delete=models.RESTRICT)

    def __str__(self):
        return self.title + ' - ' + self.techno.name

    # Allows local deletion of files
    def delete(self, using=None, keep_parents=False):
        # Delete the image associated with the instance
        if self.link_imagen:
            self.link_imagen.storage.delete(self.link_imagen.name)
        # Delete the PDF file associated with the instance
        if self.pdf_link:
            self.pdf_link.storage.delete(self.pdf_link.name)
        # Call the delete method of the parent model to delete the instance
        super().delete(using=using, keep_parents=keep_parents)

class Favorites(models.Model):
    user = models.ForeignKey(User, on_delete=models.RESTRICT, verbose_name='Favorites')
    books = models.ManyToManyField('Book', related_name='favorites')

    def __str__(self):
        return f"{self.user}'s Favorites"

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, verbose_name='Title')
    author = models.ForeignKey(Author, on_delete=models.RESTRICT, verbose_name='Author')
    year = models.IntegerField(verbose_name='Year')
    techno = models.ForeignKey(Techno, on_delete=models.RESTRICT, verbose_name='Techno')
    language = models.ForeignKey(Language, on_delete=models.RESTRICT, verbose_name='Language')
    image = models.ImageField(upload_to='media/books/images/', verbose_name='Image', null=True, blank=True)
    pdf_link = models.FileField(upload_to='media/books/pdf/', verbose_name='Pdf')
    description = models.TextField(verbose_name='Description', blank=True, default='')
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.RESTRICT)

    def __str__(self):
        return self.title + '- by ' + self.user.username

    # Allows local deletion of files
    def delete(self, using=None, keep_parents=False):
        if self.image:
            self.image.storage.delete(self.image.name)
        if self.pdf_link:
            self.pdf_link.storage.delete(self.pdf_link.name)
        super().delete(using=using, keep_parents=keep_parents)
