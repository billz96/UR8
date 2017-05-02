from django.contrib.auth.models import User
from django import forms
from .models import Profile, Video

class UploadVideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'description', 'video']

class ResetPasswordForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['password']

class EditAvatarForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

class UserRegFrom(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
