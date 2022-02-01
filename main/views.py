from django.shortcuts import redirect, render, HttpResponse


# Create your views here.

def index(request):
    return render(request, 'home.html')
    # return HttpResponse('<h1>index</h1>')
