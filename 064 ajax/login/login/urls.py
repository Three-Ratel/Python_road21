"""login URL Configuration

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
from django.contrib import admin

from app01 import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', views.Login.as_view(), name='login'),
    url(r'^logout/', views.logout, name='logout'),

    url(r'^register/', views.register, name='register'),
    url(r'^pre_register/', views.pre_register),

    url(r'^add_publisher/', views.add_publisher, name='add_publisher'),
    url(r'^edit_publisher/(\d+)', views.edit_publisher, name='edit_publisher'),

    url(r'^add_book/', views.add_book, name='add_book'),
    url(r'^edit_book/(\d+)', views.edit_book, name='edit_book'),

    url(r'^edit_author/(\d+)', views.edit_author, name='edit_author'),
    url(r'^add_author/', views.add_author, name='add_author'),
    url(r'^(author|book|publisher)/', views.List_item.as_view(), name='list'),
    url(r'^del_(author|book|publisher)/(\d+)', views.del_item, name='del'),


]
