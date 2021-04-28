from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import Users
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def index(request):
    # print(request.user.get_full_name)
    # if request.user.is_authenticated:
    return render(request, 'main/index.html')
    # else:
    #     return HttpResponseRedirect('http://127.0.0.1:8000/login/')

def about(request):
    return render(request, 'main/about.html')

def mercury_tcp(request):
    return render(request, 'main/mercury_tcp.html')

def mercury_gsm(request):
    return render(request, 'main/mercury_gsm.html')

def redidect_res(name_res):
    if name_res == 'VRES':
        return redirect('/VRES/')

@login_required(login_url='/login/')
def vres(request):
    return render(request, 'VRES/tcp.html')