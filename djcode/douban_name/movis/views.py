from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
	return HttpResponse('Hello movis!!!')


def movis_param(request, name, id):
	return HttpResponse(name,str(id))

# Create your views here.
