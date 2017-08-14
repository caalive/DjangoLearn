from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse


def books_param(requst,name,id):
	return HttpResponse(name,str(id))


def hello_books(request):
	s = reverse("nb")
	return HttpResponse(u"<a href=\""+s+"\">"+"this new book add"+"</a>")

def hello_new_books(request):
	return HttpResponse('this is new books welcome')
