from django.urls import path


from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('view/<int:id>/', views.view_data, name='view'),
    path('delete/<int:id>/', views.delete_data, name='delete'),
]