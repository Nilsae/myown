# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse
from .models import post
def myown_app_view(request):
    queryset = post.objects.filter(target_age='E')
    return render(request,'posts.html',context={'post':queryset})

def static_view(request):
    # return HttpResponse('Here has to do with my static files')
    return render(request,'styles.css')
# Create your views here.
