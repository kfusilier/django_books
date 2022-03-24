from django.db import models

# Create your models here.
CATEGORY_CHOICES = (
	("fic", "fiction"),
	("nfic", "non-fiction")
)

# GENRE_CHOICES = (
# 	("fic", "fiction"),
# 	("nfic", "non-fiction")
# )

class Book(models.Model):

	title = models.CharField(max_length=50)
	author = models.CharField(max_length=50)
	img = models.CharField(max_length=250)
	published = models.IntegerField()
	category = models.CharField(max_length=10, choices = CATEGORY_CHOICES)
	created_at = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return self.name

	class Meta:
		ordering = ['title']