from email.mime import base
from django import http
from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html')