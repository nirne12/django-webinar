
from django.shortcuts import render
from django.http import HttpResponse
#from django.shortcuts import httpResponse


# Create your views here.

def hello_world(request) :
    return HttpResponse("Hello World")
