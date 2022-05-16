from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from .models import *
menu = ["Menu", "Watchlist", "Sign In"]

def index(request):
    posts = Top10Cartoons.objects.all()
    return render(request, 'Top10Cartoons/index.html', {'posts': posts, 'menu': menu, 'title': 'Ну страница вот эта главная'})

def about(request):
    return render(request, 'Top10Cartoons/about.html', {'menu': menu, 'title': 'О сайте вот этом'})



def categories(request, categories):
    if str(categories) == "Want404":
        raise Http404()
    if str(categories) == "Home":
        return redirect('home', permanent=False)
    return HttpResponse(f"<h1>Мультфильмы по категориям</h1><p>{categories}<p>")


def pageNotFound (request, exception):
    return HttpResponseNotFound('<h1>Пытайся лучше(404 ошибочка)</h1>')