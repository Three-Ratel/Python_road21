from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return '{}'.format(self.name)


class Book(models.Model):
    title = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    sale = models.IntegerField()
    inventory = models.IntegerField()
    pub = models.ForeignKey('Publisher', on_delete=models.CASCADE, related_name='books', related_query_name='xxx',
                            null=True)

    def __str__(self):
        return '{}'.format(self.title)


class Author(models.Model):
    name = models.CharField(max_length=32)
    books = models.ManyToManyField('Book')

    def __str__(self):
        return '{}'.format(self.name)
