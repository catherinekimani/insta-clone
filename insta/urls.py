from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    
    path('register/',views.register,name='register'),
    path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),
    
    path('profile',views.profile,name='profile'),
    path('follow/<int:user_id>/', views.follow, name='follow'),
    path('suggestions/', views.index, name='suggestions'),
    path('like/<post_id>', views.like, name='like'),
    path('comment/<post_id>',views.new_comment, name = 'comment'),
    
    path('addPost/', views.addPost, name='addPost'),
    
    path('search/', views.search_results, name = 'search_results'),
]