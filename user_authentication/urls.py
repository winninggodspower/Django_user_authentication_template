from django.contrib import admin
from django.urls import re_path, path

from user_authentication import views

urlpatterns = [
    re_path(r'accounts/home/?',  views.home, name='home'),
    re_path('accounts/login/?', views.login_user, name='login'),
    re_path('accounts/register/?', views.register, name='register'),
    re_path('accounts/logout/?', views.logout_user, name='logout'),
    
    path("password_reset", views.password_reset_request, name="password_reset")
]