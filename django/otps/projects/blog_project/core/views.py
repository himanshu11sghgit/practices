from django.shortcuts import render

from core.models import Blog

# Create your views here.


def home(request):
    blogs = Blog.objects.all()
    context = {"blogs": blogs}
    return render(request, "core/home.html", context)


def post(request, id):
    blog = Blog.objects.get(id=id)
    context = {"blog": blog}
    return render(request, "core/post.html", context)