from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse  #HttpResponseRedirect,
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User as sUser
from random import randint
#from django.utils.http import urlquote

from .models import User as dUser
from .models import Lyric as dLyric

def fullPage(length, limit=9):
    if (length == limit):
        return 1
    else:
        return 0

def mainPage(request):
    return render(request, 'mainPage.html', {
        "lyricTotal": len( dLyric.objects.all() ),
        "userTotal": len( dUser.objects.all() )
    })


def showLogin(request):
    return render(request, 'login.html', {})


def showRegister(request):
    return render(request, 'register.html', {})

def showRandom(request):
    count = dLyric.objects.count()
    if count == 0:
        return render(request, "showLyric.html", {
            "lyric": {
                'id': 0,
                'text': "I'm sorry, but nothing is found... \n Add a sentence here."
            }
        })
    rndIndex = randint(1,count-1)
    respLyric = dLyric.objects.get(pk = rndIndex)
    return render(request, "showLyric.html", {
        "lyric": respLyric
    })


def showLogout(request):
    logout(request)
    return render(request, 'logout.html', {})

def showSubmit(request):
    return render(request, 'submitLyric.html', {})

def reSubmit(request,id):
    return render(request, 'reSubmitLyric.html', {
        "lyric": dLyric.objects.get(pk=id)
    })

def showLyric(request, id):
    lyric = dLyric.objects.get(pk=id)
    return render(request, 'showLyric.html', { "lyric": lyric })

def showLyrics(request, page=1, limit=9):
    idFrom = limit * (page - 1)
    idTo = limit * page
    data = dLyric.objects.all()[idFrom:idTo]
    return render(request, 'showLyrics.html', {
        "lyricData": data,
        "page": page,
        "fullPage": fullPage(len(data),limit)
    })

def searchText(request, text="", page=1, limit=9):
    fr = limit * (page - 1)
    tr = limit * page
    dl = dLyric.objects.filter(text__contains=text)[fr:tr]
    return render(request, 'searchResult.html', {
      "lyricData": dl,
      "keyword": text,
      "about": "text",
      "page": page,
      "fullPage": fullPage(len(dl),limit)
      })

def searchAuthor(request, text="", page=1, limit=9):
    fr = limit * (page - 1)
    tr = limit * page
    dl = dLyric.objects.filter(author__contains=text)[fr:tr]
    return render(request, 'searchResult.html', {
      "lyricData": dl,
      "keyword": text,
      "about": "author",
      "page": page,
      "fullPage": fullPage(len(dl),limit)
      })

def searchSource(request, text="", page=1, limit=9):
    fr = limit * (page - 1)
    tr = limit * page
    dl = dLyric.objects.filter(source__contains=text)[fr:tr]
    return render(request, 'searchResult.html', {
      "lyricData": dl,
      "keyword": text,
      "about": "source",
      "page": page,
      "fullPage": fullPage(len(dl),limit)
      })

def searchCategory(request, text="", page=1, limit=9):
    fr = limit * (page - 1)
    tr = limit * page
    dl = dLyric.objects.filter(category__contains=text)[fr:tr]
    return render(request, 'searchResult.html', {
      "lyricData": dl,
      "keyword": text,
      "about": "category",
      "page": page,
      "fullPage": fullPage(len(dl),limit)
      })

def showContrib(request, username="", page=1, limit=9):
    fr = limit * (page - 1)
    tr = limit * page
    theUser = sUser.objects.get(username=username)
    dl = dLyric.objects.filter(user=theUser)[fr:tr]
    return render(request, 'searchResult.html', {
      "lyricData": dl,
      "keyword": username,
      "about": "user",
      "page": page,
      "fullPage": fullPage(len(dl),limit)
      })

def searchInterface(request):
    return render(request, "searchInterface.html")

def showUser(request,username):
    thisUser = sUser.objects.get(username=username)
    thisDUser = dUser.objects.get(uid=thisUser.id)
    return render(request, "showUser.html", {
        "userS": thisUser,
        "userD": thisDUser,
        "contribCount": len( dLyric.objects.filter(user=thisUser) )
    })
x = """
def showContrib(request,username):
    thisUser = sUser.objects.get(username=username)
    thisDUser = dUser.objects.get(uid=thisUser.id)
    return render(request, "showUserContrib.html", {
        "userS": thisUser,
        "userD": thisDUser
    })
"""
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
    return showUser(request,username=request.user)


def tpl(request):
    template = loader.get_template('tpl.html')
    context = {}
    return HttpResponse(template.render(context, request))
