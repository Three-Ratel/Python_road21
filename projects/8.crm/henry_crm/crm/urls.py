from django.conf.urls import url

from crm import views

urlpatterns = [
    url(r'^login/', views.login, name='login'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^reg/', views.reg, name='reg'),

    # 客户库的展示，公户
    url(r'^customer/', views.CustomerList.as_view(), name='customer'),
    # 私户的展示
    url(r'^list_customer/', views.CustomerList.as_view(), name='list_customer'),
    # 添加客户
    url(r'^add_customer/', views.modify_customer, name='add_customer'),
    # 编辑客户
    url(r'^edit_customer/(\d+)', views.modify_customer, name='edit_customer'),

    # 某个销售的所有跟进记录
    url(r'^consult_record/$', views.ConsultRecordList.as_view(), name='consult_record'),
    # 某个客户的跟进记录
    url(r'^consult_record/(\d+)/', views.ConsultRecordList.as_view(), name='consult_record'),
    # 添加一条客户跟进记录
    url(r'^add_consult/(?P<customer_id>\d+)/', views.modify_consult, name='add_consult'),
    # 编辑某个客户的跟进记录
    url(r'^edit_consult/(\d+)/', views.modify_consult, name='edit_consult'),

    # 报名表
    url(r'^list_enrollment/$', views.EnrollmentList.as_view(), name='list_enrollment'),
    # 添加报名表
    url(r'^add_enrollment/(?P<customer_id>\d+)/', views.modify_enrollment, name='add_enrollment'),
    # 编辑报名表
    url(r'^edit_enrollment/(\d+)/', views.modify_enrollment, name='edit_enrollment'),

]
