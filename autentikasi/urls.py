from django.urls import path
from . import views

app_name = 'autentikasi'

urlpatterns = [
    path('', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]