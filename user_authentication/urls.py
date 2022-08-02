from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls import url
from user_authentication import views

urlpatterns = [
    re_path(r'home/',  views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_user, name='logout'),
    url('^', include('django.contrib.auth.urls'))

]