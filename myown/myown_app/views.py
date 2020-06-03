# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render,HttpResponse,redirect
from .models import posts , article , listLink
from .forms import SignUpForm
def myown_app_view(request):
    queryset1 = posts.objects.filter(target_age='E')
    queryset2 = article.objects.filter()
    return render(request,'posts.html',context={'posts':queryset1,'article':queryset2})

def static_view(request):
    # return HttpResponse('Here has to do with my static files')
    return render(request,'styles.css')
def list_of_things_view(request):
    list = listLink.objects.filter()
    return render(request,'List_template.html',context={'listLink':list})
def testing_view(request):
    return render(request, 'test_view.html')
def register_view(request):
    return render(request, 'signup.html')
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.save()
            # username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
# Create your views here.
