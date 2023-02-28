from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.


# The Techno model with a name field and an auto-generated primary key
class Techno(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    # Return the name of the instance as a string
    def __str__(self):
        return self.name

    # Set the default ordering for instances of this model by name
    class Meta:
        ordering = ['name']

# The Language model with a name field and an auto-generated primary key
class Language(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    # Return the name of the instance as a string
    def __str__(self):
        return self.name

# The Author model with a name field and an auto-generated primary key
class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, verbose_name='Author')

    # Return the name of the instance as a string
    def __str__(self):
        return self.name

    # Set the default ordering for instances of this model by name
    class Meta:
        ordering = ['name']

# The CheatSheet model with several fields, including a foreign key to Techno and a file upload field
class CheatSheet(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, verbose_name='Title')
    techno = models.ForeignKey(Techno, on_delete=models.RESTRICT, verbose_name='Techno')
    link_imagen = models.ImageField(upload_to='media/cheat_sheets/images/', verbose_name='Image', null=True, blank=True)
    pdf_link = models.FileField(upload_to='media/cheat_sheets/pdf/', verbose_name='Pdf', default='', blank=True)
    description = models.TextField(verbose_name='Description', blank=True)
    user = models.ForeignKey(User, on_delete=models.RESTRICT)

    # Return the title and techno name of the instance as a string
    def __str__(self):
        return self.title + ' - ' + self.techno.name

    # Allow local deletion of files when an instance is deleted
    def delete(self, using=None, keep_parents=False):
        # Delete the image associated with the instance
        if self.link_imagen:
            self.link_imagen.storage.delete(self.link_imagen.name)
        # Delete the PDF file associated with the instance
        if self.pdf_link:
            self.pdf_link.storage.delete(self.pdf_link.name)
        # Call the delete method of the parent model to delete the instance
        super().delete(using=using, keep_parents=keep_parents)

# The Favorites model with a foreign key to User and a many-to-many relationship with Book
class Favorites(models.Model):
    user = models.ForeignKey(User, on_delete=models.RESTRICT, verbose_name='Favorites')
    books = models.ManyToManyField('Book', related_name='favorites')

    # Return a string representation of the user's favorites
    def __str__(self):
        return f"{self.user}'s Favorites"

# The Book model with several fields, including foreign keys to Techno and Language and an image upload field
class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, verbose_name='Title')
    author = models.ForeignKey(Author, on_delete=models.RESTRICT, verbose_name='Author')
    # The options argument that sets the list of options to be displayed (tuples).
    year_choices = [(r,r) for r in range(1970, datetime.date.today().year+1)]
    year = models.IntegerField(verbose_name='Year', choices=year_choices)
    techno = models.ForeignKey(Techno, on_delete=models.RESTRICT, verbose_name='Techno')
    language = models.ForeignKey(Language, on_delete=models.RESTRICT, verbose_name='Language')
    image = models.ImageField(upload_to='media/books/images/', verbose_name='Image', null=True, blank=True)
    pdf_link = models.FileField(upload_to='media/books/pdf/', verbose_name='Pdf')
    description = models.TextField(verbose_name='Description', blank=True, default='')
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.RESTRICT)

    # Return a string representation of the user title
    def __str__(self):
        return self.title + '- by ' + self.user.username
    
    # sort data method
    class Meta:
        ordering = ['techno']

    # Allow local deletion of files when an instance is deleted
    def delete(self, using=None, keep_parents=False):
        # Delete the image associated with the instance
        if self.image:
            self.image.storage.delete(self.image.name)
        # Delete the PDF file associated with the instance
        if self.pdf_link:
            self.pdf_link.storage.delete(self.pdf_link.name)
        super().delete(using=using, keep_parents=keep_parents)
