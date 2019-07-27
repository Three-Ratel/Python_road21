from django.conf.urls import url
from app import views

urlpatterns = [
	url(r'^pc-geetest/register', views.pcgetcaptcha, name='pcgetcaptcha'), # 相当于初始化
	url(r'^pc-geetest/validate$', views.pcvalidate, name='pcvalidate'),
	url(r'^pc-geetest/ajax_validate', views.pcajax_validate, name='pcajax_validate'), # 二次验证
	url(r'', views.home, name='home'),
]
