# App/Controllers/UserController.py

# Django modules
from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect

# Locals
from App.Models.User_forms import SignUpForm


# CONTROLLER: UserController
class UserController():

    # def register(request):
    #     return render(request, 'views/user/register.html')


    # def register(request):
    #     if request.method == "POST":
    #         pass
    #     else:
    #         context = {'form': SignUpForm()}
    #         return render(request, 'views/user/register.html',context)

    
    def register(request):
        if request.method == "POST":
            form = SignUpForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('user')
                return HttpResponse('<h1>Alex Pagoada</h1>%s' % username)
            else:
                context = {'form': form}
                return render(request, 'views/user/register.html',context)
        else:
            context = {'form': SignUpForm()}
            return render(request, 'views/user/register.html',context)