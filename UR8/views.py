# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from .forms import UserRegFrom, EditAvatarForm, ResetPasswordForm, UploadVideoForm
from .models import Profile, Video
from django.contrib.auth.models import User

# Create your views here.
# Login is required to view this page..
def home(request):
    if request.method == 'GET' and request.user.is_authenticated():
        return render(request, 'home.html', {})
    else:
        return render(request, 'sign-in.html', {})

def view_vid(request):
    if request.method == 'GET' and request.user.is_authenticated():
        user = request.user
        videos = user.video_set.all()
        return render(request, 'view_vid.html', {'videos':videos})
    else:
        return render(request, 'sign-in.html', {})

def upld_vid(request):
    if request.method == 'GET' and request.user.is_authenticated():
        form = UploadVideoForm()
        return render(request, 'upld_vid.html', {'form':form})
    elif request.method == 'POST' and request.user.is_authenticated():
        form = UploadVideoForm(request.POST, request.FILES)
        if form.is_valid():
            user = request.user
            v = form.cleaned_data['video']
            t = form.cleaned_data['title']
            d = form.cleaned_data['description']
            new_video = user.video_set.create(video=v, title=t, description=d)
            new_video.save()
            return render(request, 'home.html', {})
        else:
            return render(request, 'upld_vid.html', {'form':form})
    else:
        return render(request, 'sign-in.html', {})

# reset your password
def reset_pwd(request):
    if request.method == 'GET' and request.user.is_authenticated():
        form = ResetPasswordForm()
        return render(request, 'reset_pwd.html', {'form':form})
    elif request.method == 'POST' and request.user.is_authenticated():
        form = ResetPasswordForm(request.POST)
        if form.is_valid():
            new_pwd = form.cleaned_data["password"]
            uname = request.user.username
            user = User.objects.get(username=uname)
            user.set_password(new_pwd)
            user.save()
            return render(request, 'home.html', {})
        else:
            return render(request, 'reset_pwd.html', {'form':form})
    else:
        return render(request, 'sign-in.html', {})

# edit profile picture
def edit_avatar(request):
    if request.method == 'GET' and request.user.is_authenticated():
        form = EditAvatarForm()
        return render(request, 'edit_avatar.html', {'form':form})
    elif request.method == 'POST' and request.user.is_authenticated():
        form = EditAvatarForm(request.POST, request.FILES)
        if form.is_valid():
            def_img = "avatar/None/default_avatar.png"
            new_image = form.cleaned_data["image"]
            if def_img == new_image:
                error = "You haven't selected any image. Please try again."
                return render(request, 'edit_avatar.html', {'form':form, 'error':error})
            else:
                profile = request.user.profile
                profile.image = new_image
                profile.save()
                return render(request, 'home.html', {})
        else:
            return render(request, 'edit_avatar.html', {'form':form})
    else:
        return render(request, 'sign-in.html', {})

# view your profile
def profile(request):
    if request.method == 'GET' and request.user.is_authenticated():
        return render(request, 'profile.html', {})
    else:
        return render(request, 'sign-in.html', {})

# Signs in the user..
def signin_view(request):
    if request.method == 'GET':
        if request.user.is_authenticated():
            return render(request, 'home.html', {})
        else:
            return render(request, 'sign-in.html', {})
    elif request.method == 'POST':
        uname = request.POST['uname']
        pwd = request.POST['pwd']
        user = authenticate(username=uname, password=pwd)

        if user is not None:
            login(request, user)
            return render(request, 'home.html', {})
        else:
            error = 'Username or password are invalid. Please, try again.'
            return render(request, 'sign-in.html', {'error': error})
    else:
        return render(request, 'sign-in.html', {})

# Signs up the user..
def signup_view(request):
    if request.method == 'POST':

        if request.user.is_authenticated():
            logout(request)

        form = UserRegFrom(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            uname = form.cleaned_data["username"]
            user = form.save(commit=False)
            pwd = form.cleaned_data["password"]
            user.set_password(pwd)
            user.save()

            user = authenticate(username=uname, password=pwd)
            login(request, user)

            profile = Profile(user_id=user.id)
            profile.save()

            img_path = user.profile.image
            print("Image math: ", img_path)

            return render(request, 'home.html', {})

        else:
            return render(request, 'sign-up.html', {'form': form})
    else:
        form = UserRegFrom()
        return render(request, 'sign-up.html', {'form': form})

# Logs out the user..
def signout_view(request):
    logout(request)
    return render(request, 'sign-in.html', {})
