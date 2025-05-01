from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.


def index(r: HttpRequest):
    with open("eng_description.txt", "r") as description_file:
        description = description_file.read()
    return render(r, "index.html", {"eng_description": description})
