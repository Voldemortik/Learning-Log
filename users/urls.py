from django.conf.urls import url
from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView

from . import views

urlpatterns = [
     #Страница для входа
     url(r'^login/$', LoginView.as_view(), {'template_name' : 'users/login.html'},name='login'),
     #Страница для выхода
     url(r'^logout/$', LogoutView.as_view(), name='logout'),
     #Стараница регистрации
     url(r'^register/$', views.register, name='register'),
     ]