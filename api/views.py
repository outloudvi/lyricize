from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from frontend.models import *


def index(request):
    return HttpResponse("Hello, world. This is API.")


@login_required
def submitLyric(request):
    lyric = Lyric()
    lyric.text = request.POST['lyric']
    lyric.author = request.POST['author']
    lyric.source = request.POST['source']
    lyric.category = request.POST['category']
    lyric.desc = request.POST['desc']
    lyric.user = request.user
    try:
        lyric.save()
    except Exception as ext:
        return JsonResponse({
            "status": "fail",
            "errorType": type(ext),
            "errorArg": ext.args,
            "user": "",
        })
    return JsonResponse({
        "status": "success",
        "id": lyric.id
    })

@login_required
def reSubmitLyric(request,id):
    lyric = Lyric.objects.get(pk=id)
    if request.user != lyric.user and ( not request.user.is_staff()) :
        return JsonResponse({
            "status": "fail",
            "errorType": "Lyricize.BadPermission",
            "errorArg": "Not authorized.",
            "user": "",
        })
    lyric.text = request.POST['lyric']
    lyric.author = request.POST['author']
    lyric.source = request.POST['source']
    lyric.category = request.POST['category']
    lyric.desc = request.POST['desc']
    lyric.user = request.user
    try:
        lyric.save()
    except Exception as ext:
        return JsonResponse({
            "status": "fail",
            "errorType": type(ext),
            "errorArg": ext.args,
            "user": "",
        })
    return JsonResponse({
        "status": "success",
        "id": lyric.id
    })