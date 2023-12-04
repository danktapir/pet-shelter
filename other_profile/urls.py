from django.urls import path
from . import views

app_name = 'other_profile'

urlpatterns = [
    path('<str:username>/', views.profile, name='profile'),
    path('<str:username>/report/', views.report_user, name='report_user'),
]