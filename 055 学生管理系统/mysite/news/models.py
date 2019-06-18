# Create your models here.
from django.db import models


class Reporter(models.Model):
    full_name = models.CharField(max_length=70)

    def __str__(self):
        return self.full_name


class Article(models.Model):
    pub_date = models.DateField()
    headline = models.CharField(max_length=200)
    content = models.TextField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline


class User(models.Model):
    name = models.CharField(max_length=20)


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

# class Reporter(models.Model):
#     full_name = models.CharField(max_length=70)
#     articles = models.ManyToManyField('Article', through='ReporterArticle')
#
#
# class Article(models.Model):
#     pub_date = models.DateField()
#     headline = models.CharField(max_length=200)
#     content = models.TextField()
#
#
# class ReporterArticle(models.Model):
#     reporter_id = models.ForeignKey('Article')
#     article_id = models.ForeignKey('Reporter')
