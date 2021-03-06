"""myown URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# from django.conf.urls import url
from django.conf import settings
# from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('myown_app/',include('myown_app.urls')),
    path('',include('myown_app.urls')),
    path('polls/', include('polls.urls')),
    path('auth/', include('authentication.urls')),
    path('accounts/', include('allauth.urls')),  # <--
    path('index/', TemplateView.as_view(template_name="index.html")), # <--,
    # path('payments/', include('getpaid.urls')),
    # path('static/', include('authentication.urls')),
]
from django.contrib import admin
from django.conf.urls import include, url