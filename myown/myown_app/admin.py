# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import post
from .models import article

class postAdmin(admin.ModelAdmin):
    search_fields = (
        'text',
        'title'
    )
    list_display = (
        'id',
        'title'
    )
    readonly_fields = (
        'created_at',
        'updated_at'
    )
    # list_filter = (
    #     'target_age',
    #     'creator'
    # )
class articleAdmin(admin.ModelAdmin):
    search_fields = (
        'content',
        'title',
        'discription'
    )
    list_display = (
        'id',
        'title',
    )

# Register your models here.
admin.site.register(post,postAdmin)
admin.site.register(article,articleAdmin)