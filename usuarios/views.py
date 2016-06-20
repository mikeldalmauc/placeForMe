from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    suma = 2 + 2
    return render(request, 'index.html', {'suma': suma})
