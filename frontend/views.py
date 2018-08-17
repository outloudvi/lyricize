from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User as sUser

from .models import *

def mainPage(request):
    return render(request, 'mainPage.html', {})

def showLogin(request):
    return render(request, 'login.html', {})

def showRegister(request):
    return render(request, 'register.html', {})

def showLogout(request):
    logout(request)
    return render(request, 'logout.html', {})

def doLogin(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return JsonResponse({
            "status": "success",
            "user": username,
        })
    else:
        return JsonResponse({
            "status": "fail",
            "user": "",
        })

def doRegister(request):
    username = request.POST['username']
    password = request.POST['password']
    email = request.POST['email']
    desc = request.POST['description']
    lastip = request.META['REMOTE_ADDR']
    try:
        user = sUser.objects.create_user(username, email, password)
    except Exception as ext:
        return JsonResponse({
            "status": "fail",
            "errorType": type(ext),
            "errorArg": ext.args,
            "user": "",
        })
    if user is not None:
        try:
            duser = User()
            duser.uid = user.id
            duser.desc = desc
            duser.lastip = lastip
            duser.email = email
            duser.save()
            login(request, user)
        except Exception as ext:
            return JsonResponse({
            "status": "fail",
            "errorType": type(ext),
            "errorArg": ext.args,
            "user": "",
        })
        return JsonResponse({
            "status": "success",
            "user": username,
        })

@login_required
def submitLyric(request):
    return render(request, 'submitLyric.html', {})

def tpl(request):
    template = loader.get_template('tpl.html')
    context = {
    }
    return HttpResponse(template.render(context, request))