# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import login as auth_login
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt 
def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			auth_login(request, user)
			return render(request, 'insta/registration/signup_done.html')
	else:
		form = SignUpForm()
	return render(request, 'insta/registration/signup.html', {'form': form})

