from django.contrib import admin
from django.urls import path


from core import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('add-data/', views.add_data),
    path('get-data/', views.get_data)
]
