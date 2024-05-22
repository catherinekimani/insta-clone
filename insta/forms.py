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
    username = forms.CharField(required=True, label="Username")
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password1']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Enter your username'
        self.fields['password1'].widget.attrs['placeholder'] = 'Enter your password'

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user','bio']
        
class ProfileUpdateForm(forms.ModelForm):
    profile_pic = forms.ImageField(label='Choose Photo', widget=forms.FileInput(attrs={'accept': 'image/*'}))
    
    class Meta:
        model = Profile
        fields = ['bio','profile_pic']
        
class NewPostForm(forms.ModelForm):
    image = forms.ImageField(label='Select from your computer', widget=forms.FileInput(attrs={'accept': 'image/*'}))

    class Meta:
        model = Post
        exclude = ['user', 'date_posted', 'title']
        fields = ['content', 'image']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['content'].widget.attrs['placeholder'] = 'Write your caption'

class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['user', 'date_posted']
        fields = ['comment']
        widgets = {
            'comment': forms.TextInput(attrs={'placeholder': 'Add a comment...'}), 
            'tags': forms.CheckboxSelectMultiple(),
        }
        labels ={
            'comment':False
        }
        
