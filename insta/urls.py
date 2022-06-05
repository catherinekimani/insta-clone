from django.urls import path
from . import views

urlpatterns = [
    path('index',views.index,name='index'),
    
    path('',views.register,name='register'),
    path('login/',views.login,name='login'),
    
    path('profile',views.profile,name='profile'),
    
    path('likes_count/<int:pk>',views.like,name='likes_count')
]