from django.db import models


# Create your models here.
class Publisher(models.Model):
	name = models.CharField(max_length=32)

	def __str__(self):
		return self.name


class Author(models.Model):
	name = models.CharField(max_length=32)

	def __str__(self):
		return self.name


class Book(models.Model):
	title = models.CharField(max_length=32)
	price = models.DecimalField(max_digits=6, decimal_places=2)
	pub_date = models.DateTimeField(auto_now_add=True)
	pub = models.ForeignKey(Publisher, on_delete=models.CASCADE)
	authors = models.ManyToManyField(Author)
