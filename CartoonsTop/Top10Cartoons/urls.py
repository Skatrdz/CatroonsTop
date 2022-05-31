from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('categories/<slug:categories>/', categories),
    path('mainMenu/', mainMenu, name='mainMenu'),
    path('watchlist/', watchlist, name='watchlist'),
    path('login/', login, name='login'),
]