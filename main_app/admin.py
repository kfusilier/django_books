from django.contrib import admin
from .models import Book # import the Cat model from models.py
# Register your models here.

admin.site.register(Book) # this line will add the model to the admin panel