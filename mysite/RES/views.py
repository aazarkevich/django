from django.shortcuts import render
from django.http import HttpResponse
from .models import TreeMenuV, DataMercuryV, DeviceMercuryV


def vres(request):
    # return HttpResponse('Hello')
    # print(request)
    return render(request,'tcp/vres_tcp.html')

def menu(request):


    if str(request.user.groups.all()[0]) == 'VRES':
        return render(request,'tcp/menu.html', {'menu': TreeMenuV.objects.all(), 'values': DataMercuryV.objects.all()})
