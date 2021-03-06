# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
class posts(models.Model):
    objects = None
    title=models.CharField(max_length=100)
    text = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    CHOICES = (('K', 'Kids'), ('M', 'Mature'), ('E', 'Everyone'))
    target_age = models.CharField(max_length=1, choices=CHOICES)
    # image_add = models.ImageField(null=True, blank=True, upload_to="success_image/")

    # def image_tag(self):
    #     from django.utils.html import escape
    #     return u'<img src="%s" />' % escape(image.jpg)
    #     image_tag.short_description = 'Image'
    #     image_tag.allow_tags = True

# Create your models here.
class Hotel(models.Model):
    name = models.CharField(max_length=50)
    hotel_Main_Img = models.ImageField(upload_to='images/')

class article(models.Model):
    title = models.CharField(max_length=100)
    discription = models.TextField(max_length=1000)
    content = models.TextField(max_length=10000,default='content of this post in none')
class listLink(models.Model):
    name = models.CharField(max_length = 50)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
