from django.conf.urls import url
from app import views

urlpatterns = [
	url(r'^pc-geetest/register', views.pcgetcaptcha, name='pcgetcaptcha'),
	# url(r'^mobile-geetest/register', views.mobilegetcaptcha, name='mobilegetcaptcha'),
	url(r'^pc-geetest/validate$', views.pcvalidate, name='pcvalidate'),
	url(r'^pc-geetest/ajax_validate', views.pcajax_validate, name='pcajax_validate'),
	# url(r'^mobile-geetest/ajax_validate', views.mobileajax_validate, name='mobileajax_validate'),
	url(r'', views.home, name='home'),
]
