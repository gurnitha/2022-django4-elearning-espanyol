# Usuarios/Controllers/IndexController.py

# Django modules
from django.shortcuts import render, HttpResponse

# Define your controller here.


class IndexController():
	def index(request,year):
		return HttpResponse('<h1>Welcom ING, on year:</h1>%s' %year)
