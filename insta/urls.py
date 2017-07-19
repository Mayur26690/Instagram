from django.conf.urls import url, include
from django.contrib.auth.views import login
from django.contrib import admin
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
	url(r'^$', views.dashboard, name='dashboard'),
    url(r'^signup/$',views.signup, name='signup'),
    url(r'^edit/$', views.edit, name='edit'),


    url(r'^login/$',auth_views.login,{'template_name': 'insta/registration/login.html'}, name='login'),


]    