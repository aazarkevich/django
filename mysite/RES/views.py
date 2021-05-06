from django.shortcuts import render
from django.http import HttpResponse

def vres(request):
    # return HttpResponse('Hello')
    # print(request)
    return render(request,'tcp/vres_tcp.html')

def menu(request):
    return render(request,'tcp/menu.html')