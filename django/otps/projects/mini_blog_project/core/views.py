from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.contrib import messages



from .forms import SignupForm, LoginForm, BlogForm
from .models import Blog


# Create your views here.



def home(request):
    blogs = Blog.objects.all()
    context = {'blogs': blogs}
    return render(request, 'core/home.html', context)


def about(request):
    return render(request, 'core/about.html')


def contact(request):
    return render(request, 'core/contact.html')


def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    if request.method == 'POST':
        form = BlogForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            form = BlogForm()
            messages.success(request, 'blog saved successfully!!')
    else:
        form = BlogForm()
    blogs = Blog.objects.all()
    full_name = request.user.get_full_name()
    group = request.user.groups.get()
    context = {
        'form': form,
        'blogs': blogs, 
        'full_name': full_name,
        'group': group
    }
    return render(request, 'core/dashboard.html', context)


def user_signup(request):
    if request.user.is_authenticated:
        return redirect('/dashboard/')
    if request.method == 'POST':
        form = SignupForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            if Group.objects.filter(name='Author').exists():
                group = Group.objects.get(name='Author')
                user.groups.add(group)
            messages.success(request, 'Signup successfully!!')
            return redirect('/login/')
    else: 
        form = SignupForm()
    context = {'form': form}
    return render(request, 'core/signup.html', context)


def user_login(request):
    if request.user.is_authenticated:
        return redirect('/dashboard/')
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(request, **form.cleaned_data)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successfully!!')
                return redirect('/dashboard/')
            else:
                messages.error(request, 'authentication failed!!')
    else:
        form = LoginForm()
    context = {'form': form}
    return render(request, 'core/login.html', context)


def user_logout(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    logout(request)
    return redirect('/login/')


def update_data(request, id):
    if not request.user.is_authenticated:
        return redirect('/login/')
    blog = Blog.objects.get(id=id)
    if request.method == 'POST':
        form = BlogForm(data=request.POST, files=request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request, 'Blog updated successfully!!')
            return redirect('/dashboard/')
    else:
        form = BlogForm(instance=blog)
    context = {'form': form}

    return render(request, 'core/update.html', context)


def delete_data(request, id):
    if not request.user.is_authenticated:
        return redirect('/login/')
    if not request.user.has_perm('core.delete_blog'):
        return redirect('/dashboard/')
    Blog.objects.get(id=id).delete()
    messages.success(request, 'Blog deleted successfully!!')
    return redirect('/dashboard/')