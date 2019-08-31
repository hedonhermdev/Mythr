from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import FormView

from .forms import UserRegistrationForm, UserLoginForm, CommentForm, NewPostForm
from .models import Post, Comment


def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # User
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = User(username=username, email=email)
            user.set_password(password)
            user.save()
            # Profile
            user.profile.first_name = form.cleaned_data['first_name']
            user.profile.last_name = form.cleaned_data['last_name']
            user.profile.birthdate = form.cleaned_data['birthdate']
            user.profile.save()
            user.refresh_from_db()
            # Login
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('blog-home')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', context={'form': form})


def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('blog-home')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', context={'form': form})


def logout_view(request):
    logout(request)
    return redirect('blog-home')


@login_required(login_url='/blog/accounts/login/')
def home(request):
    title = 'Home Page'
    posts = list(Post.objects.all())
    context = {
        'title': title,
        'posts': posts
    }
    return render(request, 'home.html', context=context)


@login_required(login_url='/blog/accounts/login/')
def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'postdetail.html', context={'post': post})


@login_required(login_url='/blog/accounts/login/')
def new_post(request):
    user = request.user
    if request.method == 'POST':
        form = NewPostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            post = Post.objects.create(title=title, content=content, author=user)
        return redirect('blog-post-detail', id=post.id)
    else:
        form = NewPostForm()
    return render(request, 'newpost.html', {'form': form})

@login_required(login_url='/blog/accounts/login/')
def new_comment(request, id):
    user = request.user
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(content=form.cleaned_data['content'], author=form.cleaned_data['author'], post=post)
            comment.save()
            return redirect('blog-post-detail', id=post.id)
    else:
        form = CommentForm()
    return render(request, 'newcomment.html', context={'form': form})


def post_delete_view(request, id):
    post = get_object_or_404(id=id)
    if request.user == post.author:
        if request.method == 'POST':
            post.delete()
            return redirect('blog-home')
        return render(request, 'postdelete.html', {'post': post})
    else:
        return redirect('blog-home')