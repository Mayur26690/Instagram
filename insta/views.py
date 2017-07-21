# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import SignUpForm,LoginForm,UserEditForm,ProfileEditForm
from django.contrib.auth import login as auth_login
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import Profile 
from imgs.models import Image

@csrf_exempt 
def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			new_user = form.save(commit=False)
			new_user.set_password(form.cleaned_data['password1'])
			new_user.save()
			profile = Profile.objects.create(user=new_user)
			return render(request, 'insta/rege/signup_done.html')
	else:
		form = SignUpForm()
	return render(request, 'insta/rege/signup.html', {'form': form})

@login_required
def edit(request):
	if request.method == 'POST':
		user_form = UserEditForm(instance=request.user, data=request.POST)
		profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save()
			print 'Successful'
		else:
			print 'Error'
	else:
		user_form = UserEditForm(instance=request.user)
		profile_form = ProfileEditForm(instance=request.user.profile)
	return render(request, 'insta/rege/edit.html', {'user_form': user_form, 'profile_form': profile_form})

@login_required
def dashboard(request):
	user = request.user
	images = Image.objects.filter(user=user)
	return render(request, 'insta/rege/dashboard.html', {'section': 'dashboard', 'user': user, 'images': images})	

