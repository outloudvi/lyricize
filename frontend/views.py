from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import loader
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .models import *

def mainPage(request):
    return render(request, 'mainPage.html', {})

def showLogin(request):
    return render(request, 'login.html', {})

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

@login_required
def submitLyric(request):
    return render(request, 'submitLyric.html', {})

def tpl(request):
    template = loader.get_template('tpl.html')
    context = {
    }
    return HttpResponse(template.render(context, request))