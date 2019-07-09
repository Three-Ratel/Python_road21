from django.conf.urls import url

from crm import views

urlpatterns = [
    url(r'^login/', views.login, name='login'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^reg/', views.reg, name='reg'),
    url(r'^customer/', views.CustomerList.as_view(), name='customer'),
    url(r'^list_customer/', views.CustomerList.as_view(), name='list_customer'),
    url(r'^add_customer/', views.modify_customer, name='add_customer'),
    url(r'^edit_customer/(\d+)', views.modify_customer, name='edit_customer'),

    url(r'^consult_record/$', views.ConsultRecordList.as_view(), name='consult_record'),
    url(r'^consult_record/(\d+)/', views.ConsultRecordList.as_view(), name='consult_record'),
    url(r'^add_consult/(?P<customer_id>\d+)/', views.modify_consult, name='add_consult'),
    url(r'^edit_consult/(\d+)/', views.modify_consult, name='edit_consult'),

    # 报名表
    url(r'^list_enrollment/$', views.EnrollmentList.as_view(), name='list_enrollment'),
    url(r'^add_enrollment/(?P<customer_id>\d+)/', views.modify_enrollment, name='add_enrollment'),
    url(r'^edit_enrollment/(\d+)/', views.modify_enrollment, name='edit_enrollment'),

]
