from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Top 10 cartoons")

def categories(request):
    return HttpResponse("<h1>Мультфильмы по категориям</h>")