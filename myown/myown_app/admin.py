# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import posts, article , listLink

class postsAdmin(admin.ModelAdmin):
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
        # 'title',
        # 'discription'
        # 'content',
    )
class listLinkAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name'
    )
    # search_fields = (
    #     'name'
    # )

# Register your models here.
admin.site.register(posts,postsAdmin)
admin.site.register(article,articleAdmin)
admin.site.register(listLink,listLinkAdmin)