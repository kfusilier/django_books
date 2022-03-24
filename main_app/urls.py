from django.urls import path
from . import views 

# like app.use in express
urlpatterns = [
	path('', views.Home.as_view(), name='home'), # Added home path
	path('about/', views.About.as_view(), name='about'),
	path('books/', views.Book_List.as_view(), name='book_list'),

]
