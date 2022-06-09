from email import contentmanager
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

    @classmethod
    def search_profile(cls,search_term):
        profile = cls.objects.filter(user__username__icontains=search_term)
        return profile

    
    
    def __str__(self):
        return f'{self.user.username} Profile'
        
class Post(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    image = CloudinaryField('image')
    date_posted = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    def save_post(self):
        self.save()
        
    def delete_post(self):
        self.delete()
        
    @classmethod
    def update_post(cls,id,post):
        posted = Post.objects.filter(id=id).update(post = post)
        return posted

    @classmethod
    def get_images(cls):
        post = Post.objects.all()
        return post

    @classmethod
    def get_image_by_id(cls):
        post = Post.objects.filter(id=Post.id)
        return post
    
    def total_likes(self):
        return self.likes.count()
    
    def __str__(self):
        return self.content
    
class Comment(models.Model):
    comment = models.TextField(null=True)
    post = models.ForeignKey(Post, related_name='comments',on_delete=models.CASCADE,null=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    
    
    def save_comment(self):
        self.save()
        
    def delete_comment(self):
        self.delete()
        
    @classmethod
    def get_comment(cls):
        comment = Comment.objects.all()
        return comment
    
class Like(models.Model):
	user = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)
	post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)
    