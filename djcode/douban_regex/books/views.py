from django.shortcuts import render

from django.http import HttpResponse

def hello(request):
	return HttpResponse('Hello Python')

def hello_php(request):
	return HttpResponse('Hello PHP')

"""
def hello_books(requst, books_name):
#	print(requst)
	print('books:'+books_name)
	if books_name:
		return HttpResponse("<h1>hello "+books_name+" <h1>")
"""
def hello_books_id(requst,name,id):
	return HttpResponse(name + str(id))
