from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime
from .models import TreeMenuV, DataMercuryV, TreeMenuZ, DataMercuryZ
from django.views.generic import View
from django.db.models import Q
from .forms import AddSubstation


def index(request):
    return render(request, 'base.html', {'name_res': request.user.groups.all()[0]})


class MercuryTCP_IP(View):

    def get(self, request):
        return render(request, 'tcp/menu.html', {'menu': self.show_substation(name_res=request.user.groups.all()[0]),
                                                 'values': self.values_tp(name_res=request.user.groups.all()[0])})

    @staticmethod
    def show_substation(name_res):
        if str(name_res) == 'Восточный':
            return TreeMenuV.objects.all()
        elif str(name_res) == 'Западный':
            return TreeMenuZ.objects.all()

    def values_tp(self, name_res):
        if str(name_res) == 'Восточный':
            return DataMercuryV.objects.filter(
                date=datetime.now().strftime("%Y-%m-%d")).order_by(
                'id')
        elif str(name_res) == 'Западный':
            return DataMercuryZ.objects.filter(
                date=datetime.now().strftime("%Y-%m-%d")).order_by(
                'id')


class Substation(View):

    @staticmethod
    def add_substation(request):
        if request.method == 'POST':
            form = AddSubstation(request.POST)

            if form.is_valid():
                print('True')
                return HttpResponseRedirect(f'http://127.0.0.1:8000/res/addTcp/')
        else:
            form = AddSubstation()

            return form


def add_tcp(request):
    return render(request, 'tcp/addTcp.html',
                  {'menu': MercuryTCP_IP.show_substation(name_res=request.user.groups.all()[0]),
                   'form_add_substation': Substation.add_substation(request)})


def show_substation(request, id_substation):
    # return TreeMenuV.objects.filter(Q(id=2) | Q(parent_id=2))

    return render(request, 'tcp/showSubstation.html',
                  {'menu': MercuryTCP_IP.show_substation(name_res=request.user.groups.all()[0]),
                   'podstation': MercuryTCP_IP.show_substation(name_res=request.user.groups.all()[0]).filter(
                       Q(id=id_substation) | Q(parent_id=id_substation)),
                   'devices': {}})
