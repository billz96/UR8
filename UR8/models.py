# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User)
    image = models.ImageField(upload_to="avatars", default = "avatar/None/default_avatar.png")
    # images will be uploaded to: 'uploads/media/avatars'

    def __str__(self):
        return self.user.username

class Video(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.FileField(upload_to="videos")
    # videos will be uploaded to: 'uploads/media/videos'
    title = models.TextField(max_length=500)
    description = models.TextField(max_length=3000)

    def __str__(self):
        return self.user.username+" "+self.title+" "+self.description

# class Review(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     text = ...
#     rating = ... ( 0-5 stars )

    # def __str__(self):
    #     return self.user.username
