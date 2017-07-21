# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Image

# Create your views here.
@login_required
def  img_list(req):
	images = Image.objects.all()
	return render(req, 'imgs/list.html',{'images': images})