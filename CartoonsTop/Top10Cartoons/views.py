from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

def index(request):
    return HttpResponse("Top 10 cartoons")


def categories(request, categories):
    if str(categories) == "Want404":
        raise Http404()
    if str(categories) == "Home":
        return redirect('home', permanent=False)
    return HttpResponse(f"<h1>Мультфильмы по категориям</h1><p>{categories}<p>")


def pageNotFound (request, exception):
    return HttpResponseNotFound('<h1>Пытайся лучше(404 ошибочка)</h1>')