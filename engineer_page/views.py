from django.shortcuts import render
from django.http import HttpRequest


def index(r: HttpRequest):
    with open("eng_description.txt", "r") as description_file:
        description = description_file.read()
    return render(r, "eng_index.html", {"eng_description": description})
