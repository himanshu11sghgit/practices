from django.urls import path


from core import views



urlpatterns = [
    path("", views.index),
    path("register/", views.register),
    path("login/", views.user_login),
    path("logout/", views.user_logout),
    path("images/", views.images_view),
]