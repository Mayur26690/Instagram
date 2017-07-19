from django.conf.urls import url, include
from django.contrib.auth.views import login
from django.contrib import admin
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # url(r'^signup/$',views.signup, name = 'signup'),
    url(r'^signup/$',views.signup, name='signup'),
    url('^', include('django.contrib.auth.urls')),
    url(r'^login/$',auth_views.login),

]    