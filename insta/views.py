# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import SignUpForm,LoginForm,UserEditForm,ProfileEditForm
from django.contrib.auth import login as auth_login
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import Profile,Contact
from imgs.models import Image
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages


@csrf_exempt 
def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			profile = Profile.objects.create(user=user)
			return render(request, 'insta/rege/signup_done.html', {'new_user': user})
	else:
		form = SignUpForm()
	return render(request, 'insta/rege/signup.html', {'form': form})



@login_required
def user_list(request):
	users = User.objects.filter(is_active=True)
	query = request.GET.get('q')
	if query:
		users = users.filter(username__icontains=query)
	return render(request, 'insta/rege/user/list.html', { 'users': users})

@login_required
def edit(req):
	if req.method == 'POST':
		print 'post'
		user_form = UserEditForm(instance=req.user, data=req.POST)
		profile_form = ProfileEditForm(instance=req.user.profile, data=req.POST, files=req.FILES)
		if user_form.is_valid() and profile_form.is_valid():
			print 'valid'
			new_item = user_form.save(commit=False)
			new_item.user = req.user
			new_item.save()
			new_profile = profile_form.save(commit=False)
			new_profile.user = req.user
			new_profile.save()
			print 'Successful'
		else:
			print 'Error'
	else:
		print 'else'
		new_item = UserEditForm(instance=req.user)
		new_profile = ProfileEditForm(instance=req.user.profile)
	return render(req, 'insta/rege/edit.html', {'user_form': new_item, 'profile_form': new_profile})

@require_POST
@login_required
def user_follow(request):
    user_id = request.POST.get('id')
    action = request.POST.get('action')
    if user_id and action:
        try:
            user = User.objects.get(id=user_id)
            if action == 'follow':
                Contact.objects.get_or_create(user_from=request.user,
                                              user_to=user)
            else:
                Contact.objects.filter(user_from=request.user,
                                       user_to=user).delete()
            return JsonResponse({'status':'ok'})
        except User.DoesNotExist:
            return JsonResponse({'status':'ko'})
    return JsonResponse({'status':'ko'})

@login_required
def user_detail(request, username):
	user = get_object_or_404(User, username=username, is_active=True)
	images = Image.objects.filter(user=user)
	return render(request, 'insta/rege/user/detail.html', {'section': 'people', 'user': user, 'images': images})	

@login_required
def dashboard(request):
	user = request.user
	images = Image.objects.filter(user=user)
	return render(request, 'insta/rege/dashboard.html', {'section': 'dashboard', 'user': user, 'images': images})	

