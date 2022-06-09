from audioop import reverse
from django.shortcuts import render,redirect,get_object_or_404

from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm,NewPostForm, UpdateProfileForm,ProfileUpdateForm,  NewCommentForm,LoginUserForm

from django.contrib.auth.decorators import login_required

from . models import Profile,Post,Comment,Like

from django.http import HttpResponseRedirect

from django.contrib.auth import login,logout,authenticate
# Create your views here.
@login_required(login_url='/register/')
def index(request):
    all_users = Profile.objects.all()
    post = Post.objects.order_by('-date_posted')
    return render(request,'index.html', {'post':post,'all_users':all_users})

def register(request):
    form = CreateUserForm()
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request,'register.html', {'form':form})

def login_user(request):
    form = LoginUserForm()

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password1')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        
    return render(request, 'login.html', {'form': form})

def logout_user(request):
    logout (request)
    return redirect('login')
@login_required(login_url='/login/')
def profile(request):
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST,instance=request.user)
        form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if form.is_valid() and form.is_valid():
            form.save()
            form.save()
            return redirect('profile')
    else:
        form = UpdateProfileForm(instance=request.user)
        form = ProfileUpdateForm(instance=request.user.profile)
    return render(request,'profile/profile.html', {'form':form})


@login_required(login_url='login')        
def like(request, post_id):
    user = request.user
    post = Post.objects.get(pk=post_id)
    like = Like.objects.filter(user=user, post=post)
    if like:
        like.delete()
    else:
        new_like = Like(user=user, post=post)
        new_like.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

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
    return render(request, 'addPost.html', {"user":current_user,"form":form})

def new_comment(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewCommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = current_user
            comment.save()
        return redirect('index')

    else:
        form = NewCommentForm()
    return render(request, 'comment.html', {"user":current_user,"form": form})

def search_results(request):
    if 'username' in request.GET and request.GET["username"]:
        search_term = request.GET.get("username")
        searched_profiles =Profile.search_profile(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"profile": searched_profiles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})