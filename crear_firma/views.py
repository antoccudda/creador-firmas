from django.http import request
from django.shortcuts import render

# Create your views here.

def index(requets):
    return render(requets, 'index.html')

def crear_firma(request):
    pass
