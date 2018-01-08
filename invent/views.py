from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView # Import TemplateView

 

def index(request):
    return HttpResponse('hello from invent')

def about(request):
    return render(request, 'test.html',{'nazwa':'dupa'})

