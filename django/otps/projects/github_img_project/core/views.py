from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

from core.models import Github

import requests
from bs4 import BeautifulSoup as bs


# Create your views here.


def index(request):
    # print("***************")

    if request.method == "POST":
        github_user = request.POST.get("github_user")

        url = f"https://github.com/{github_user}"
        r = requests.get(url=url)
        # print(r.content)
        soup = bs(r.content)
        image_link = soup.find("img", {"alt": "Avatar"})["src"]
        # print(f"image_link", image_link)

        github = Github(github_user=github_user, image_link=image_link, user=request.user)
        github.save()
        messages.info(request, f"{github_user}'s image is saved successfully")


    


    return render(request, "index.html")



def register(request):
    if (request.method == "POST"):
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")

        if (password == password2):
            if User.objects.filter(username=username):
                messages.info(request, "Username is already taken!!")
                return redirect("/register/")
            elif User.objects.filter(email=email):
                messages.info(request, "Email is already taken!!")
                return redirect("/register/")
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                messages.info(request, "User created successfully!!")

                return redirect("/login/")
        else:
            messages.info(request, "Password does not match with confirm password")
            return redirect("/register/")


    return render(request, "signup.html")


def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.info(request, "Login successfull!!")
            return redirect("/")
        else:
            messages.info(request, "Invalid Credentials!!")
            return redirect("/login/")
    return render(request, "login.html")


def user_logout(request):
    logout(request)
    return redirect("/login/")


def images_view(request):
    githubs = Github.objects.filter(user=request.user)
    context = {"githubs": githubs}
    return render(request, "images.html", context)