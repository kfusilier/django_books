from django.db import models
from django.contrib.auth.models import User

# Create your models here.
CATEGORY_CHOICES = (
	("Fiction", "Fiction"),
	("Non-Fiction", "Non-fiction")
)

# GENRE_CHOICES = (
# 	("fic", "fiction"),
# 	("nfic", "non-fiction")
# )

class Book(models.Model):

	title = models.CharField(max_length=100)
	author = models.CharField(max_length=50)
	img = models.CharField(max_length=250)
	published = models.IntegerField()
	category = models.CharField(max_length=50, choices = CATEGORY_CHOICES)
	created_at = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return self.title

	class Meta:
		ordering = ['title']