"""student_class URL Configuration

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

from app1 import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # 登陆
    url(r'^login/', views.login),
    url(r'^logout/', views.logout),
    # 班级
    url(r'^list_grade/', views.list_grade),
    url(r'^add_grade/', views.add_grade),
    url(r'^del_grade/', views.del_grade),
    url(r'^edit_grade/', views.edit_grade),

    # 学生
    url(r'^list_student/', views.list_student),
    url(r'^add_student/', views.add_student),
    url(r'^del_student/', views.del_student),
    url(r'^edit_student/', views.edit_student),


]
