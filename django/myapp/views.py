from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('<h1>welcome to my django app</h1>')

def about(request):
    return HttpResponse('<h1>about</h1><p>built in with django</p>')

def hello_world(request):
    return HttpResponse('Hello , World')