from django.urls import path
from . import views

app_name = 'my_profile'

urlpatterns = [
    path('my-profile/', views.index, name='index'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
]