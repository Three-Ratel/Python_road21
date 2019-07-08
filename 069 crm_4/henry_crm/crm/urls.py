from django.conf.urls import url

from crm import views

urlpatterns = [
    url(r'^login/', views.login, name='login'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^reg/', views.reg, name='reg'),
    url(r'^customer/', views.CustomerList.as_view(), name='customer'),
    url(r'^show_customer/', views.CustomerList.as_view(), name='show_customer'),
    url(r'^add_customer/', views.modify_customer, name='add_customer'),
    url(r'^edit_customer/(\d+)', views.modify_customer, name='edit_customer'),
    url(r'^del/', views.del_item, name='del'),

]
