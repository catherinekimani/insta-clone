from audioop import reverse
from django.shortcuts import render,redirect,get_object_or_404

from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm,NewPostForm

from django.contrib.auth.decorators import login_required

from . models import Profile,Post

from django.http import HttpResponseRedirect
# Create your views here.
@login_required(login_url='/register/')
def index(request):
    post = Post.objects.all()
    return render(request,'index.html', {'post':post})

def register(request):
    form = CreateUserForm()
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request,'register.html', {'form':form})

def login(request):
    
    return render(request,'login.html')

@login_required(login_url='/login/')
def profile(request):
    profile = Profile.objects.all()
    return render(request,'profile/profile.html',{'profile':profile})

@login_required(login_url='/login/')
def like(request,pk):
    post = get_object_or_404(Post,id = request.POST.get('post_id'))
    post.likes.add(request.user)
    return redirect('index')

@login_required(login_url='/login/')
def addPost(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
        return redirect('index')

    else:
        form = NewPostForm()
    return render(request, 'addPost.html', {"form": form})