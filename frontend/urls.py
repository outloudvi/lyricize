from django.urls import path

from . import views

urlpatterns = [
    path('', views.mainPage, name='index'),
    path('tpl/', views.tpl, name='template'),
]