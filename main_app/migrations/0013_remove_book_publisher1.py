# Generated by Django 4.0.3 on 2022-04-02 04:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0012_rename_author_book_authors'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='publisher1',
        ),
    ]