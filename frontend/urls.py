from django.urls import path
# from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.mainPage, name='index'),
    path('login/', views.showLogin, name='login'),
    path('logout/', views.showLogout, name='logout'),
    path('login.do/', views.doLogin, name='login_do'),
    path('register/', views.showRegister, name='register'),
    path('register.do/', views.doRegister, name='register_do'),
    path('my/', views.myAccount, name='register_do'),
    path('tpl/', views.tpl, name='template'),
    path('l/', views.showLyrics, name='r_Lyrics'),
    path('lyric/<int:id>/', views.showLyric, name='lyric'),
    path('l/<int:page>/', views.showLyrics, name='lyrics'),
    path('s/t/<str:text>/', views.searchText, name='searchText'),
    path('s/a/<str:text>/', views.searchAuthor, name='searchAuthor'),
    path('s/s/<str:text>/', views.searchSource, name='searchSource'),
    path('s/c/<str:text>/', views.searchCategory, name='searchCategory'),
    path('s/', views.searchInterface, name='searchInterface'),
    path('new/', views.showSubmit, name='submitLyrics'),
    path('new/<int:id>/', views.reSubmit, name='editLyrics'),
    path('u/<str:username>/', views.showUser, name='showUser'),
    path('u/<str:username>/contrib/', views.showContrib, name='showContrib'),
    path('u/<str:username>/contrib/<int:page>/', views.showContrib, name='showContrib_page'),
    path('random/', views.showRandom),
]