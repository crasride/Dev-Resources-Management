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


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, verbose_name='Title')
    author = models.ForeignKey(Author, on_delete=models.RESTRICT, verbose_name='Author')
    year = models.IntegerField(verbose_name='Year')
    techno = models.ForeignKey(Techno, on_delete=models.RESTRICT, verbose_name='Techno')
    language = models.ForeignKey(Language, on_delete=models.RESTRICT, verbose_name='Language')
    image = models.ImageField(upload_to='imagenes/', verbose_name='Image', null=True)
    pdf_link = models.FileField(upload_to='pdfs/', verbose_name='Pdf')
    description = models.TextField(verbose_name='Description', blank=True)
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
