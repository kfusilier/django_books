from django.urls import path
from . import views 

# like app.use in express
urlpatterns = [
	path('', views.Home.as_view(), name='home'), # Added home path
	path('books/', views.Book_List.as_view(), name='book_list'),
	# path('about/', views.Book_List.as_view(), name='about'),
	path('books/new/', views.Book_Create.as_view(), name="book_create"),
	path('books/<int:pk>/', views.Book_Detail.as_view(), name="book_detail"),
	path('books/<int:pk>/update', views.Book_Update.as_view(), name="book_update"),
	path('books/<int:pk>delete', views.Book_Delete.as_view(), name="book_delete"),

	path('user/<username>/', views.profile, name='profile'),

	path('authors/', views.authors_index, name='authors_index'),
	path('authors/<int:author_id>', views.authors_show, name='authors_show'),
	path('authors/create/', views.Author_Create.as_view(), name='authors_create'),
	path('authors/<int:pk>/update/', views.Author_Update.as_view(), name='authors_update'),
	path('authors/<int:pk>/delete/', views.Author_Delete.as_view(), name='authors_delete'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
]
