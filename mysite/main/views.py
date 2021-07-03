from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import Users
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def index(request):
    # print(request.user.get_full_name)
    # if request.user.is_authenticated:
    return HttpResponseRedirect(f'/res/')

def about(request):
    return render(request, 'main/about.html')

def mercury_tcp(request):
    return render(request, 'main/mercury_tcp.html')

def mercury_gsm(request):
    return render(request, 'main/mercury_gsm.html')


@login_required(login_url='/login/')
def vres(request):
    return redirect('RES/VRES/')