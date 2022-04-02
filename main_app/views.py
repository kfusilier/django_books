from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views import View # View class to handle requests
from django.http import HttpResponse # a class to handle sending a type of response
from django.http import HttpResponseRedirect
from django.views.generic import DetailView
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
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

@method_decorator(login_required, name='dispatch')
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

@method_decorator(login_required, name='dispatch')
class Book_Update(UpdateView):
	model = Book
	fields = ['title', 'authors', 'img', 'published', 'category', 'user']
	template_name = "book_update.html"
	def get_success_url(self):
		return reverse('book_detail', kwargs={'pk': self.object.pk})

@method_decorator(login_required, name='dispatch')
class Book_Delete(DeleteView):
	model = Book
	template_name = "book_delete_confirm.html"
	success_url = "/books/"

# profile for the user
@login_required
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

@method_decorator(login_required, name='dispatch')
class Author_Create(CreateView):
    model = Author
    fields = '__all__'
    template_name = "author_form.html"
    success_url = '/authors'

@method_decorator(login_required, name='dispatch')
class Author_Update(UpdateView):
    model = Author
    fields = ['name']
    template_name = "author_update.html"
    success_url = '/authors'

@method_decorator(login_required, name='dispatch')
class Author_Delete(DeleteView):
    model = Author
    template_name = "author_confirm_delete.html"
    success_url = '/authors'

# login, logout and signup
def login_view(request):
     # if post, then authenticate (user submitted username and password)
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        # form = LoginForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username = u, password = p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/user/'+u)
                else:
                    print('The account has been disabled.')
            else:
                print('The username and/or password is incorrect.')
    else: # it was a get request so send the emtpy login form
        # form = LoginForm()
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            print('HEY', user.username)
            return HttpResponseRedirect('/user/'+str(user))
        else:
            HttpResponse('<h1>Try Again</h1>')
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})
