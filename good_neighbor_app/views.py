from django.shortcuts import render
from django.http import HttpResponse
from models import *
from mongoengine import *

# Create your views here.


def test_view(request):
    connect('good_neighbor_db')
    article = User(username='Jhon')
    article.save()
    return HttpResponse('<h1>Saved!<h1>')