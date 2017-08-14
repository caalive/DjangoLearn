from django.shortcuts import render
from django.http import HttpResponse

def books_param(requst,name):
	print('name:   ',name)
	return HttpResponse(name)
