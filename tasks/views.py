from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h2>This is a heading 2 from Python Django</h2>")
