from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from .models import AuthUser


# Create your views here.

class CustomBackend(ModelBackend):
	def authenticate(self, username=None, password=None, **kwargs):
		try:
			print(2222)
			user = AuthUser.objects.get(Q(username=username) | Q(email=username))
			if user.check_password(password):
				return user
		except Exception as e:
			print(e)
			return None


def index(request):
	return render(request, 'permanage/index.html')


def register(request):
	return render(request, 'permanage/register.html')


def register_action(request):
	firstname = request.POST.get('firstname', '')
	lastname = request.POST.get('lastname', '')
	username = request.POST.get('username', '')
	passwd = request.POST.get('passwd2', '')
	email = request.POST.get('email', '')
	if User.objects.filter(username=username):
		state = 'user_exist'
	else:
		new_user = User.objects.create_user(username=username, password=passwd, email=email, first_name=firstname,
											last_name=lastname)
		new_user.save()
		return HttpResponseRedirect('/')
	content = {
		'state': state,
		'user': None,
	}
	return render(request, 'permanage/register.html', content)


def login_action(request):
	if request.method == 'POST':
		username = request.POST.get('username', '')
		passwd = request.POST.get('passwd', '')
		user = authenticate(username=username, password=passwd)
		if user:
			return HttpResponseRedirect('event_message')
		else:
			return render(request, 'permanage/login.html', {'error': 'username or password erorr!'})


def event_message(request):  # 该函数定义的是成功页面的提示页面
	return render(request, "permanage/index.html")


def log_in(request):
	return render(request, 'permanage/login.html')


def table(request):
	return render(request, 'permanage/tables.html')


def chart(request):
	return render(request, 'permanage/charts.html')


def department(request):
	return render(request, 'permanage/department.html')


def personManage(request):
	return render(request, 'permanage/manage_person.html')


def salaryManage(request):
	return render(request, 'permanage/manage_wage.html')


def transferManage(request):
	return render(request, 'permanage/manage_transfer.html')


def fundManage(request):
	return render(request, 'permanage/manage_accumulation_fund.html')


def labourManage(request):
	return render(request, 'permanage/manage_labour.html')


def trainManage(request):
	return render(request, 'permanage/manage_train.html')
