from django.shortcuts import render
from django.http import HttpResponse

from django.template import Template,Context
from django.shortcuts import render



#1
"""
def hello_books(request, bn):
	t = Template('<html>\
		<body>\
		<h1> welcome view  {{books_name}} </h1>\
		</body>\
</html>')	

	c = Context({'books_name':bn})
	html = t.render(c)

	return HttpResponse(html)

"""

"""
#2
from django.template.loader import get_template
def hello_books(request, bn):
	t = get_template("hello.html")#添加自定义网页文件
#	c = Context('books_name')
	html = t.render({'books_name':bn})
	
	return HttpResponse(html)	

"""

"""
#3
from django.template.loader import render_to_string
def hello_books(request, bn):
	html = render_to_string('welcome.html')
	
	return HttpResponse(html)	

"""

"""
#4
from django.shortcuts import render_to_response
def hello_books(request, bn):
	return render_to_response('hello.html',{'books_name':bn})
	
"""

#5
from django.shortcuts import render_to_response, render
def hello_books(request, bn):
	return render(request,'hello.html',{'books_name':bn})
	









