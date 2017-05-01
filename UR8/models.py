# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
# from django.db.models.signals import post_save
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User)
    image = models.ImageField(upload_to="avatars", default = "avatar/None/default_avatar.png")
    # images will be uploaded to: uploads/media/avatars

    def __str__(self):
        return self.user.username

# Create your models here.
# class Profile(models.Model):
#     user = models.OneToOneField(User)
#     image = models.ImageField(blank=True, null=True) # and models.FileField() for anything else maybe..
    #
    #
    # def __str__(self):
    #     return self.user.username

# def create_profile(sender, **kwargs):
#     if kwargs["created"]:
#       new_profile = Profile.objects.create(user=kwargs["instance"])
#
# post_save.connect(create_profile, sender=User)
