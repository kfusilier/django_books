from django.contrib import admin
from .models import Book, Author
# import the Cat model from models.py
# Register your models here.

admin.site.register(Book) # this line will add the model to the admin panel
admin.site.register(Author) # this line will add the model to the admin panel
