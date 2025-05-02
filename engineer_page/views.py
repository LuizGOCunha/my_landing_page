from django.shortcuts import render
from django.http import HttpRequest

from .utils import gather_engineer_description, gather_engineer_projects


def index(r: HttpRequest):
    paragraphs = gather_engineer_description()
    projects_info = gather_engineer_projects()

    return render(
        r,
        "eng_index.html",
        {
            "paragraphs": paragraphs,
            "projects": projects_info,
        },
    )
