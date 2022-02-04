# Usuarios/Controllers/IndexController.py

# Django modules
from django.shortcuts import render, HttpResponse

# Define your controller here.


class IndexController():
	def index(request):
		return render(request,'views/index/index.html')