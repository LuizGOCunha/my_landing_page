# from django.shortcuts import render
from django.http import HttpResponse
from django.core.handlers.wsgi import WSGIRequest

# Create your views here.


def index(r: WSGIRequest):
    return HttpResponse("<h1>This is the landing page</h1>")
