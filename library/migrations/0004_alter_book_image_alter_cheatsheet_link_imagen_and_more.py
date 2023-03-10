# Generated by Django 4.1.6 on 2023-02-26 09:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('library', '0003_cheatsheet_pdf_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='imagenes/', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='cheatsheet',
            name='link_imagen',
            field=models.ImageField(blank=True, null=True, upload_to='cheat_sheets/', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='cheatsheet',
            name='pdf_link',
            field=models.FileField(blank=True, default='', upload_to='cheat_sheets/pdfs/', verbose_name='Pdf'),
        ),
        migrations.CreateModel(
            name='Favorites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('books', models.ManyToManyField(to='library.book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
