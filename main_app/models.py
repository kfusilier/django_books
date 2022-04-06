from django.db import models
from django.contrib.auth.models import User


# Author Model
class Author(models.Model):
	name = models.CharField(max_length=100)
	
	def __str__(self):
		return self.name

# Create your models here.
CATEGORY_CHOICES = (
	("Fiction", "Fiction"),
	("Non-Fiction", "Non-fiction")
)

# Book Model
class Book(models.Model):

	title = models.CharField(max_length=100)
	img = models.CharField(max_length=250)
	published = models.IntegerField()
	category = models.CharField(max_length=50, choices = CATEGORY_CHOICES) # 1-many
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	authors = models.ManyToManyField(Author)
	created_at = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return self.title

	class Meta:
		ordering = ['title']
