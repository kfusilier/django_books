from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views import View # View class to handle requests
from django.http import HttpResponse # a class to handle sending a type of response

from django.views.generic import DetailView
from django.urls import reverse

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Book #import Book model

# Create your views here.
# Here we will be creating a class called Home and extending it from the View class
class Home(TemplateView):
	template_name = 'home.html'

class About(TemplateView):
	template_name = 'about.html'

class Book_List(TemplateView):
	template_name = "booklist.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		title = self.request.GET.get("title")
		if title != None:
			context["books"] = Book.objects.filter(title__icontains=title)
			# We add a header context that includes the search param
			context["header"] = f"Searching for {title}"
		else:
			context["books"] = Book.objects.all()
			# default header for not searching 
			context["header"] = "Book List"
		return context

class Book_Create(CreateView):
	model = Book
	fields = ['title', 'author', 'img', 'published', 'publisher', 'category']
	template_name = "book_create.html"
	def get_success_url(self):
		return reverse('book_detail', kwargs={'pk': self.object.pk})

class Book_Detail(DetailView): 
	model = Book
	template_name="book_detail.html"

class Book_Update(UpdateView):
	model = Book
	fields = ['title', 'author', 'img', 'published', 'publisher', 'category']
	template_name = "book_update.html"
	def get_success_url(self):
		return reverse('book_detail', kwargs={'pk': self.object.pk})

class Book_Delete(DeleteView):
    model = Book
    template_name = "book_delete_confirm.html"
    success_url = "/books/"