from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views import View # View class to handle requests
from django.http import HttpResponse # a class to handle sending a type of response
from django.http import HttpResponseRedirect
from django.views.generic import DetailView
from django.urls import reverse
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Book, Author #import Book model

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
	fields = ['title', 'authors', 'img', 'published', 'category', 'user']
	template_name = "book_create.html"
	# def get_success_url(self):
	# 	return reverse('book_detail', kwargs={'pk': self.object.pk})

	def form_valid(self, form):
		self.object = form.save(commit=False)
		self.object.user = self.request.user
		self.object.save()
		return HttpResponseRedirect('/books')

class Book_Detail(DetailView): 
	model = Book
	template_name="book_detail.html"

class Book_Update(UpdateView):
	model = Book
	fields = ['title', 'authors', 'img', 'published', 'category', 'user']
	template_name = "book_update.html"
	def get_success_url(self):
		return reverse('book_detail', kwargs={'pk': self.object.pk})

class Book_Delete(DeleteView):
	model = Book
	template_name = "book_delete_confirm.html"
	success_url = "/books/"

# profile for the user
def profile(request, username):
    user = User.objects.get(username=username)
    books = Book.objects.filter(user=user)
    return render(request, 'profile.html', {'username': username, 'books': books})

# Author 
def authors_index(request):
    authors = Author.objects.all()
    return render(request, 'author_index.html', {'authors': authors})

def authors_show(request, author_id):
    author = Author.objects.get(id=author_id)
    return render(request, 'author_show.html', {'author': author})

class Author_Create(CreateView):
    model = Author
    fields = '__all__'
    template_name = "author_form.html"
    success_url = '/authors'

class Author_Update(UpdateView):
    model = Author
    fields = ['name']
    template_name = "author_update.html"
    success_url = '/authors'

class Author_Delete(DeleteView):
    model = Author
    template_name = "author_confirm_delete.html"
    success_url = '/authors'