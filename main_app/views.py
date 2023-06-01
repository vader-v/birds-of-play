from django.shortcuts import render

from django.http import HttpResponse

def home(request):
  return HttpResponse('<h1>Hello chirp</h1>')

def about(request):
  return HttpResponse('<h1>About birds of play</h1>')