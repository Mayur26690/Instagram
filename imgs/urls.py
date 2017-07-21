from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.img_list, name='list'),

]	