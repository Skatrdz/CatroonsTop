from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Top 10 cartoons")