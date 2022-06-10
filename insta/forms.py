from dataclasses import fields
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from . models import *
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        
class LoginUserForm(UserCreationForm):
    username = forms.CharField(required=True)
    class Meta:
        model = User
        fields = ['username', 'password1']
        
class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user','bio']
        
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio','profile_pic']
        
class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user', 'date_posted']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }
        
class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['user', 'date_posted']
        fields = ['comment']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }
        
