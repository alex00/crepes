#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth import authenticate
from blog.forms import LoginForm

def login(request):
	if request.method == 'POST':
		login = request.POST['login']
		password = request.POST['password']
		user = authenticate(username=login, password=password)
		if user is not None:
			if user.is_active:
				auth.login(request, user)
				# Redirect to a success page.
		else:
			form = LoginForm(request.POST)
	else:
		form = LoginForm()
	return render(request, 'blog/user/login.html', locals())

def logout(request):
	auth.logout(request)
	return HttpResponseRedirect("/")