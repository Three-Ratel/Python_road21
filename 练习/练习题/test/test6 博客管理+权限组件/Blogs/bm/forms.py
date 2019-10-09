from django.forms import ModelForm

from bm import models


class BlogForm(ModelForm):
	class Meta:
		model = models.Blog
		fields = '__all__'


class ArticleForm(ModelForm):
	class Meta:
		model = models.Article
		fields = '__all__'
