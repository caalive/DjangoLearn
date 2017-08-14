from django.shortcuts import render
from django.http import HttpResponse

from django.template import Template,Context

class Book:
	def __init__(self,name):
		self.name = name
	
	def get_name(self):
		return self.name

from django.shortcuts import render_to_response, render
"""
def hello_books(request, bn):
	dict_e = {'1001':'python web guide',
			  '1002':'python web django'		
			}

	book = Book('C++')
	return render(request,'hello.html',{'books_name':book})
	
"""

def hello_books(request, bn):
	l = ['python','java','php']
	return render(request,'hello.html',{'books_name':l})








