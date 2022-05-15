from django.urls import path

from .views import *

urlpatterns = [
    path('home/', index, name='home'),
    path('about/', about, name='about'),
    path('categories/<slug:categories>/', categories),
]