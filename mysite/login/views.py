from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Users
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View

def index(request):
    return render(request,'login/index.html')

class Autorization(View):

    def post(self, request):
        name = request.POST.get('name', '')
        password = request.POST.get('password', '')
        user = authenticate(username=name, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(f'/res/')
        else:
            return HttpResponse('Неверный логин или пароль')

    def get(self, request):
        logout(request)
        return redirect('/')

