from turtle import ScrolledCanvas
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views import View # <- View class to handle requests
from django.http import HttpResponse # <- a class to handle sending a type of response

# Create your views here.

# Here we will be creating a class called Home and extending it from the View class

class Home(TemplateView):
	template_name = 'home.html'

# 	 Old Get Request
#  	Here we are adding a method that will be ran when we are dealing with a GET request
#      def get(self, request): 
# 		Here we are returning a generic response 
# 		This is similar to response.send() in express
#     return HttpResponse('Books Home')

class About(TemplateView):
	template_name = 'about.html'
	# Old Get Request
	# def get(self, request):
	# 	return HttpResponse('Books About')

class Book:
    def __init__(self, title, author, published, genre):
        self.title = title
        self.author = author
        self.published = published
        self.genre = genre

books = [
    Book("The Catcher in the Rye", "J.D. Salinger", 1991, "Fiction"),
    Book("Moby Dick", "Herman Melville", 1976, "Fiction"),
    Book("Little Women", "Louisa May Alcott", 1868, "Fiction"),
    Book("War and Peace", "Leo Tolstoy", 1869, "Fiction"),
    Book("Call of the Wild", "Jack London", 1903, "Fiction"),
]



class Book_List(TemplateView):
    template_name = 'booklist.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = books # this is where we add the key into our context object for the view to use
        return context