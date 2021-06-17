from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.views.generic import View
from RES.views import MercuryTCP_IP
from django.db.models import Q


def index(request):
    return render(request, 'mercury/podstations.html',{'menu': MercuryTCP_IP.get_model_substation(name_res=request.user.groups.all()[0]).objects.all()})

def tcp_ip(request, id_substation):
    return render(request, 'mercury/tcpIp.html',
                  {'menu': MercuryTCP_IP.get_model_substation(name_res=request.user.groups.all()[0]).objects.all(),
                   'podstation': MercuryTCP_IP.get_model_substation(
                       name_res=request.user.groups.all()[0]).objects.filter(
                       Q(id=id_substation) | Q(parent_id=id_substation)),
                   })
