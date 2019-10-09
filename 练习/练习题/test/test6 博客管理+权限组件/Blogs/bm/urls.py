"""Blogs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url

from bm import views

urlpatterns = [
	# 博客管理
	url(r'^blog/list/$', views.blog_list, name='blog_list'),
	url(r'^blog/add/$', views.blog_change, name='blog_add'),
	url(r'^blog/edit/(\d+)$', views.blog_change, name='blog_edit'),
	url(r'^(blog|article)/delete/(\d+)$', views.delete, name='delete'),
	# 文章管理
	url(r'^article/list/$', views.article_list, name='article_list'),
	url(r'^article/add/$', views.article_change, name='article_add'),
	url(r'^article/edit/(\d+)$', views.article_change, name='article_edit'),

]
