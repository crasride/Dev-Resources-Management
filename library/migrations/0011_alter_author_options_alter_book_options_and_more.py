# Generated by Django 4.1.6 on 2023-02-27 19:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0010_alter_language_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['techno']},
        ),
        migrations.AlterModelOptions(
            name='techno',
            options={'ordering': ['name']},
        ),
    ]