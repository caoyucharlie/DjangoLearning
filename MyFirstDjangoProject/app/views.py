from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def first_hello(request):
    return HttpResponse('hello world')

def girl_hello(request):
    return HttpResponse('hello girl')
