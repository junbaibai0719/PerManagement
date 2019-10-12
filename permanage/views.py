from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.models import User


# Create your views here.


def index(request):
	return render(request, 'permanage/index.html')


def register(request):
	return render(request, 'permanage/register.html')


def register_action(request):
	username = request.POST.get('username', '')
	passwd = request.POST.get('passwd2', '')
	email = request.POST.get('email', '')
	if User.objects.filter(username=username):
		state = 'user_exist'
	else:
		new_user = User.objects.create_user(username=username, password=passwd, email=email)
		new_user.save()
		return HttpResponseRedirect('index')
	content = {
		'state': state,
		'user': None,
	}
	return render(request, 'permanage/register.html', content)


def login_action(request):
	if request.method == 'POST':
		username = request.POST.get('username', '')
		passwd = request.POST.get('passwd', '')
		user = auth.authenticate(username=username, password=passwd)
		if user:
			return HttpResponseRedirect('event_message')
		else:
			return render(request, 'permanage/login.html', {'error': 'username or password eror'})


def event_message(request):  # 该函数定义的是成功页面的提示页面
	return render(request, "permanage/index.html")


def login(request):
	return render(request, 'permanage/login.html')


def table(request):
	return render(request, 'permanage/tables.html')


def chart(request):
	return render(request, 'permanage/charts.html')


def department(request):
	return render(request, 'permanage/department.html')
