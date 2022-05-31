from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from .models import *
menu = [
    {'title': "Menu", 'url_name': 'mainMenu'},
    {'title': "Watchlist", 'url_name': 'watchlist'},
    {'title': "Sign in", 'url_name': 'login'},

]

def index(request):
    posts = Top10Cartoons.objects.all()
    tags = {
        'posts': posts,
        'menu': menu,
        'title': 'main page'
    }
    return render(request, 'Top10Cartoons/index.html', context=tags)

def about(request):
    return render(request, 'Top10Cartoons/about.html', {'menu': menu, 'title': 'О сайте вот этом'})

def mainMenu(request):
    return HttpResponse("Тут вообще нужна другая структура но я пока не понимаю какая обьяснить кто нить")
def watchlist(request):
    return HttpResponse("Вотчлист, если не авторизован на авторизацию марш")
def login(request):
    return HttpResponse("Ну логайся уже: тут же должна быть дето кнопка на регистрацию")


def categories(request, categories):
    if str(categories) == "Want404":
        raise Http404()
    if str(categories) == "Home":
        return redirect('home', permanent=False)
    return HttpResponse(f"<h1>Мультфильмы по категориям</h1><p>{categories}<p>")


def pageNotFound (request, exception):
    return HttpResponseNotFound('<h1>Пытайся лучше(404 ошибочка)</h1>')