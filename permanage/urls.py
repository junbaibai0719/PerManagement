from django.urls import path

from . import views

app_name = 'permanage'

urlpatterns = [
	path('',views.index,name='index'),
	path('login',views.log_in,name='login'),
	path('login_action',views.login_action,name='login_action'),
	path('register',views.register,name='register'),
	path('register_action',views.register_action,name='register_action'),
	path('event_message',views.event_message,name='event_message'),
	path('table',views.table,name='table'),
	path('chart',views.chart,name='chart'),
	path('department',views.department,name='department'),
	path('personManage',views.personManage,name='personManage'),
	path('salaryManage',views.salaryManage,name='salaryManage'),
	path('transferManage',views.transferManage,name='transferManage'),
	path('fundManage',views.fundManage,name='fundManage'),
	path('labourManage',views.labourManage,name='labourManage'),
	path('trainManage',views.trainManage,name='trainManage'),
]
