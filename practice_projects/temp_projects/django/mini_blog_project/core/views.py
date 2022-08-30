from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import Group


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
            messages.success(request, 'Blog saved successfully!!')
    else:
        form = BlogForm()
    
    blogs = Blog.objects.all()
    full_name = request.user.get_full_name()
    groups = request.user.groups.all()
    context = {'form': form, 'blogs': blogs, 'full_name': full_name, 'groups': groups}
    return render(request, 'core/dashboard.html', context)


def update_data(request, id):
    if not request.user.is_authenticated:
        return redirect('/login/')
    if request.method == 'POST':
        blog = Blog.objects.get(id=id)
        form = BlogForm(data=request.POST, files=request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request, 'blog updated successfully!!')
            return redirect('/dashboard/')

    else:
        blog = Blog.objects.get(id=id)
        form = BlogForm(instance=blog)
    context = {'form': form}
    return render(request, 'core/update.html', context)
    


def delete_data(request, id):
    if not  request.user.is_authenticated:
        return redirect('/login/')
    if request.user.has_perm('core.delete_blog'):
        Blog.objects.get(id=id).delete()
        messages.success(request, 'blog deleted successfully!!')

    return redirect('/dashboard/')


def user_signup(request):
    if request.user.is_authenticated:
        return redirect('/dashboard/')
    if request.method == 'POST':
        form = SignupForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Signup successfully!!')
            if Group.objects.filter(name='Author').exists():
                group = Group.objects.get(name=f'Author')
                user.groups.add(group)
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
                messages.success(request, 'Signup successfully!!')
                return redirect('/dashboard/')
    else:
        form = LoginForm()
    context = {'form': form}
    return render(request, 'core/login.html', context)


def user_logout(request):
    logout(request)
    return redirect('/login/')

