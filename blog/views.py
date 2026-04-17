from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
import datetime

# Create your views here.

def home(request):
    return HttpResponse('<h1>welcome to my blog</h1>')

def about(request):
    today = datetime.date.today()
    html = f'<h1>about</h1> <p>michael</p> <p>django</P> <p>{today}</p>'
    return HttpResponse(html)
