from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import *

def mainPage(request):
    return render(request, 'mainPage.html', {})

def tpl(request):
    template = loader.get_template('tpl.html')
    context = {
    }
    return HttpResponse(template.render(context, request))