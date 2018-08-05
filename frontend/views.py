from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import *

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def tpl(request):
    template = loader.get_template('tpl.html')
    context = {
    }
    return HttpResponse(template.render(context, request))