from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from models import *
# Create your views here.


def index(request):
    return render_to_response('index.html')


def tasks(request):
    return render_to_response('tasks.html')


def neighbors(request):
    return render_to_response('neighbors.html')