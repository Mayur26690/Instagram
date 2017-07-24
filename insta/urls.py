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
    url(r'^logout/$',auth_views.logout,{'template_name': 'insta/registration/logout.html'}, name='logout'),

    url(r'^password-change/$', auth_views.password_change,{'template_name': 'insta/registration/password_change_form'}, name='password_change'),
    url(r'^password-change/done/$', auth_views.password_change_done,{'template_name': 'insta/registration/password_change_done'}, name='password_change_done'),
    url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),

    url(r'^users/$', views.user_list, name='user_list'),
    url(r'^users/follow/$', views.user_follow, name='user_follow'),
    url(r'^users/(?P<username>[-\w]+)/$', views.user_detail, name='user_detail'),

]    