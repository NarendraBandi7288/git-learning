from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def welcome(request):
    s='<h1>hello this  my first responce</h1>'
    return HttpResponse(s)
