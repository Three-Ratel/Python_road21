from django.conf.urls import url

from crm.views import auth, consultant, teacher

urlpatterns = [
    url(r'^login/', auth.login, name='login'),
    url(r'^logout/', auth.logout, name='logout'),
    url(r'^reg/', auth.reg, name='reg'),

    # 客户库的展示，公户
    url(r'^customer/', consultant.CustomerList.as_view(), name='customer'),
    # 私户的展示
    url(r'^list_customer/', consultant.CustomerList.as_view(), name='list_customer'),
    # 添加客户
    url(r'^add_customer/', consultant.modify_customer, name='add_customer'),
    # 编辑客户
    url(r'^edit_customer/(\d+)', consultant.modify_customer, name='edit_customer'),

    # 某个销售的所有跟进记录
    url(r'^consult_record/$', consultant.ConsultRecordList.as_view(), name='consult_record'),
    # 某个客户的跟进记录
    url(r'^consult_record/(\d+)/', consultant.ConsultRecordList.as_view(), name='p_consult_record'),
    #
    url(r'^add_consult/(?P<customer_id>\d+)/', consultant.modify_consult, name='add_consult'),
    # 编辑某个客户的跟进记录
    url(r'^edit_consult/(\d+)/', consultant.modify_consult, name='edit_consult'),

    # 报名表
    url(r'^list_enrollment/$', consultant.EnrollmentList.as_view(), name='list_enrollment'),
    # 添加报名表
    url(r'^add_enrollment/(?P<customer_id>\d+)/', consultant.modify_enrollment, name='add_enrollment'),
    # 编辑报名表
    url(r'^edit_enrollment/(\d+)/', consultant.modify_enrollment, name='edit_enrollment'),

    # 班级表管理
    url(r'^list_class/$', teacher.ClassList.as_view(), name='list_class'),
    url(r'^add_class/', teacher.modify_class, name='add_class'),
    url(r'^edit_class/(\d+)/', teacher.modify_class, name='edit_class'),

    # 课程记录表
    url(r'^list_course_record/(\d+)/$', teacher.CourseRecord.as_view(), name='list_course_record'),
    url(r'^add_course_record/(?P<class_id>\d+)/$', teacher.modify_course_record, name='add_course_record'),
    url(r'^edit_course_record/(?P<pk>\d+)/$', teacher.modify_course_record, name='edit_course_record'),

    # 学习记录表
    url(r'^list_study_record/(\d+)/$', teacher.StudyRecord.as_view(), name='list_study_record'),

]
