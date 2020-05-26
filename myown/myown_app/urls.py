from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path
from .views import myown_app_view,static_view,list_of_things_view
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns=[
    path('posts/',myown_app_view,name='myown_app_posts'),
path('',list_of_things_view,name='myown_app_posts'),
path('static/', static_view, name='static'),
path('admin/',admin.site.urls)
]
urlpatterns+=staticfiles_urlpatterns()
# _ROOT)if settings.DEBUG:
#     urlpatterns = url  ('',
#                            url(r'^posts/',include( myown_app_view, namespace='my own_app_posts')),
#                            path(r'^static/',include( static_view, namespace='static'))
#
#                            ) + static(settings.STATIC_URL, document_root=settings.STATIC