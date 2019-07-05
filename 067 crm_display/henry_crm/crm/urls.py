from django.conf.urls import url
from crm import views

urlpatterns = [
    url(r'^login/', views.login, name='login'),
    url(r'^reg/', views.reg, name='reg'),
    url(r'^customer/', views.customer_list, name='customer'),
    url(r'^add_customer/', views.add_customer, name='add_customer'),
    url(r'^show_customer/', views.show_customer, name='show_customer'),
]
