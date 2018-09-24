from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse  #HttpResponseRedirect,
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User as sUser
#from django.utils.http import urlquote

from .models import User as dUser
from .models import Lyric as dLyric


def mainPage(request):
    return render(request, 'mainPage.html', {})


def showLogin(request):
    return render(request, 'login.html', {})


def showRegister(request):
    return render(request, 'register.html', {})


def showLogout(request):
    logout(request)
    return render(request, 'logout.html', {})


def showLyrics(request, page=1, limit=10):
    idFrom = limit * (page - 1)
    idTo = limit * page
    data = dLyric.objects.all()[idFrom:idTo]
    return render(request, 'showLyrics.html', {"lyricData": data})

def searchText(request, text="", page=1, limit=10):
    fr = limit * (page - 1)
    tr = limit * page
    dl = dLyric.objects.filter(text__contains=text)[fr:tr]
    return render(request, 'searchResult.html', {
      "lyricData": dl,
      "keyword": text,
      "about": "text",
      "page": page
      })

def searchAuthor(request, text="", page=1, limit=10):
    fr = limit * (page - 1)
    tr = limit * page
    dl = dLyric.objects.filter(author__contains=text)[fr:tr]
    return render(request, 'searchResult.html', {
      "lyricData": dl,
      "keyword": text,
      "about": "author",
      "page": page
      })

def searchSource(request, text="", page=1, limit=10):
    fr = limit * (page - 1)
    tr = limit * page
    dl = dLyric.objects.filter(source__contains=text)[fr:tr]
    return render(request, 'searchResult.html', {
      "lyricData": dl,
      "keyword": text,
      "about": "source",
      "page": page
      })

def searchCategory(request, text="", page=1, limit=10):
    fr = limit * (page - 1)
    tr = limit * page
    dl = dLyric.objects.filter(category__contains=text)[fr:tr]
    return render(request, 'searchResult.html', {
      "lyricData": dl,
      "keyword": text,
      "about": "category",
      "page": page
      })

def searchInterface(request):
    return render(request, "searchInterface.html")

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
            thisDUser = dUser()
            thisDUser.uid = user.id
            thisDUser.desc = desc
            thisDUser.lastip = lastip
            thisDUser.email = email
            thisDUser.save()
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


@login_required
def myAccount(request):
    thisUser = sUser.objects.get(username=request.user)
    thisDUser = dUser.objects.get(uid=thisUser.id)
    return render(request, 'myAccount.html', {"desc": thisDUser.desc})


def tpl(request):
    template = loader.get_template('tpl.html')
    context = {}
    return HttpResponse(template.render(context, request))
