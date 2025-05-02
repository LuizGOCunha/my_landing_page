from django.shortcuts import render
from django.http import HttpRequest


def index(r: HttpRequest):
    return render(r, "aut_index.html")
