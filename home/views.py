from email.mime import base
from django import http
from django.shortcuts import render, HttpResponse
from .models import Members

# Create your views here.

def home(request):
    data = Members.objects.all()
    print(data)
    return render(request, 'home.html',{'members':data})