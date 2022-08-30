from django.urls import path


from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('update/<str:id>/', views.update, name='update'),
    path('delete/<str:id>/', views.delete, name='delete'),
]