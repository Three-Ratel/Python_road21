from django.db import models


# Create your models here.

class Classes(models.Model):
    c_name = models.CharField(max_length=32)


class Student(models.Model):
    s_name = models.CharField(max_length=32)
    score = models.DecimalField(max_digits=3, decimal_places=0)
    my_class = models.ForeignKey('Classes', related_name='student')


class Teacher(models.Model):
    t_name = models.CharField(max_length=32)
    sex = models.CharField(max_length=32)
    age = models.IntegerField()
    classes = models.ManyToManyField('Classes', related_name='teacher')

    def __str__(self):
        return self.t_name
