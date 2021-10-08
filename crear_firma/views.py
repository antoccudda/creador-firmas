from django.http import request
from django.shortcuts import render

# Create your views here.

def index(requets):
    return render(requets, 'outlook.html')

def crear_firma(request):
    return render(request, 'thunder.html')
