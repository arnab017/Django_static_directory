from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index_string(request):
    return HttpResponse('This a index string HttpResponse')

def index(request):
    return render(request, 'index.html')
