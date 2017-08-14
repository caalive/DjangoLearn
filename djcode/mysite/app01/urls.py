from django.conf.urls import url
from app01 import views

urlpatterns = [
	url(r'^app1', views.app1),
]
