from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from . import views


def index(request):
    return render(request, 'main/index.html')

def new(request):
    return render(request, 'main/new.html')

def page3(request):
    return render(request, 'main/page3.html')

def page4(request):
    return render(request, 'main/page4.html')
