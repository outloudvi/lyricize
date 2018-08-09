from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.mainPage, name='index'),
    path('login/', views.showLogin, name='login'),
    path('logout/', views.showLogout, name='logout'),
    path('login.do/', views.doLogin, name='login_do'),
    path('tpl/', views.tpl, name='template'),
]