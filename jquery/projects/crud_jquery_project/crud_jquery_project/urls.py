from django.contrib import admin
from django.urls import path


from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('update/', views.update),
    path('delete/', views.delete),
]
