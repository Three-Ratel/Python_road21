from django.shortcuts import render, redirect

from bm import models
from bm.forms import BlogForm, ArticleForm


def blog_list(request):
	all_blog = models.Blog.objects.all()
	return render(request, 'blog_list.html', {'all_blog': all_blog})


def blog_change(request, pk=None):
	obj = models.Blog.objects.filter(pk=pk).first()
	form_obj = BlogForm(instance=obj)
	if request.method == 'POST':
		form_obj = BlogForm(request.POST, instance=obj)
		if form_obj.is_valid():
			form_obj.save()
			return redirect('blog_list')
	title = '修改博客' if pk else '添加博客'
	return render(request, 'form.html', {'form_obj': form_obj, 'title': title})


def delete(request, table, pk=None):
	obj = getattr(models, table.capitalize())
	obj.objects.filter(pk=pk).delete()
	return redirect('{}_list'.format(table))


def article_list(request):
	all_article = models.Article.objects.all()
	return render(request, 'article_list.html', {'all_article': all_article})


def article_change(request, pk=None):
	obj = models.Article.objects.filter(pk=pk).first()
	form_obj = ArticleForm(instance=obj)
	if request.method == 'POST':
		form_obj = ArticleForm(request.POST, instance=obj)
		if form_obj.is_valid():
			form_obj.save()
			return redirect('article_list')
	title = '修改文章' if pk else '添加文章'
	return render(request, 'form.html', {'form_obj': form_obj, 'title': title})


"""rbac相关"""
from rbac.models import User
from rbac.services.init_session import init_session


def login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		obj = User.objects.filter(username=username, password=password).first()
		if obj:
			init_session(request, obj)
			return redirect('article_list')
	return render(request, 'login.html')
