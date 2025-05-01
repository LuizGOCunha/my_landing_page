from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.


def index(r: HttpRequest):
    return render(r, "index.html")
