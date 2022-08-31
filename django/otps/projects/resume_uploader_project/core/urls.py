from django.urls import path


from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('view/<int:id>/', views.view, name='view'),
    path('delete/<int:id>/', views.delete, name='delete'),
]