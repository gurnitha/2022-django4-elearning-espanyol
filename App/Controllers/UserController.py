# App/Controllers/UserController.py

# Django modules
from django.shortcuts import render, HttpResponse

# Locals
from App.Models.User_forms import SignUpForm


# CONTROLLER: UserController
class UserController():

    # def register(request):
    #     return render(request, 'views/user/register.html')


    def register(request):
        if request.method == "POST":
            pass
        else:
            context = {'form': SignUpForm()}
            return render(request, 'views/user/register.html',context)