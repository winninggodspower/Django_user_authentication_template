from django.contrib import admin
from django.urls import include, re_path
from django.conf.urls import url
from user_authentication import views

urlpatterns = [
    re_path(r'home/?',  views.home, name='home'),
    re_path('login/?', views.login_user, name='login'),
    re_path('register/?', views.register, name='register'),
    re_path('logout/?', views.logout_user, name='logout'),
    url('^', include('django.contrib.auth.urls'))

]