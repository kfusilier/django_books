# Generated by Django 4.0.3 on 2022-03-26 20:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_book_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='author',
            new_name='author1',
        ),
    ]
