from email import contentmanager
from turtle import title
from django.db import models

from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

import datetime as dt

# Create your models here.
class Profile(models.Model):
    profile_pic = CloudinaryField('image')
    bio = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def save_profile(self):
        self.save()
        
    def delete_profile(self):
        self.delete()
    
    def update_image(self,profile_pic,bio,user):
        self.profile_pic = profile_pic
        self.bio = bio
        self.user = user
        
class Post(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    image = CloudinaryField('image')
    date_posted = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    likes = models.ManyToManyField(User,related_name='likes_count')
    
    def save_post(self):
        self.save()
        
    def delete_post(self):
        self.delete()
        
    def update_image(self,title,content,image,user):
        self.title = title
        self.content = content
        self.image = image
        self.user = user
        
    def total_likes(self):
        return self.likes.count()
class Comment(models.Model):
    comment = models.TextField()
    post = models.ForeignKey(Post, related_name='comments',on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)
    
    
    def save_comment(self):
        self.save()
        
    def delete_comment(self):
        self.delete()
        
    def __str__(self):
        self.comment
        
