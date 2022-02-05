# App/Controllers/UserController.py

# Django modules
from django.shortcuts import render, HttpResponse


# CONTROLLER: UserController
class UserController():

    def register(request):
        return render(request, 'views/user/register.html')