from django.urls import path
from .views import login_view,logout_view,register_view,static_view

urlpatterns =[
    # path('login/', login_view, name='login_view'),
    # path('logout/', logout_view, name='logout_ view'),
    path('register/', register_view, name='register'),
path('static/', static_view, name='static')
]