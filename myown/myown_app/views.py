# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse
from .models import posts , article , listLink
def myown_app_view(request):
    queryset1 = posts.objects.filter(target_age='E')
    queryset2 = article.objects.filter()
    return render(request,'posts.html',context={'posts':queryset1,'article':queryset2})

def static_view(request):
    # return HttpResponse('Here has to do with my static files')
    return render(request,'styles.css')
def list_of_things_view(request):
    list = listLink.objects.filter()
    return render(request,'list_of_things.html',context={'listLink':list})
# Create your views here.
