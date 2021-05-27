from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime
from .models import TreeMenuV, TreeMenuS, TreeMenuU, TreeMenuZ, DataMercuryV, DataMercuryZ, DataMercuryS, DataMercuryU
from django.views.generic import View
from django.db.models import Q
from .forms import AddSubstation, EditSubstation


def index(request):
    return render(request, 'base.html', {'name_res': request.user.groups.all()[0]})


class MercuryTCP_IP(View):

    def get(self, request):
        return render(request, 'tcp/menu.html',
                      {'menu': self.get_model_substation(name_res=request.user.groups.all()[0]).objects.all(),
                       'values': self.values_tp(name_res=request.user.groups.all()[0])})

    @staticmethod
    def get_model_substation(name_res):
        name_res = str(name_res)
        if name_res == 'Восточный':
            return TreeMenuV
        elif name_res == 'Западный':
            return TreeMenuZ
        elif name_res == 'Северный':
            return TreeMenuS
        elif name_res == 'Южный':
            return TreeMenuU

    def values_tp(self, name_res):
        name_res = str(name_res)
        if name_res == 'Восточный':
            return DataMercuryV.objects.filter(
                date=datetime.now().strftime("%Y-%m-%d")).order_by(
                'id')
        elif name_res == 'Западный':
            return DataMercuryZ.objects.filter(
                date=datetime.now().strftime("%Y-%m-%d")).order_by(
                'id')
        elif name_res == 'Северный':
            return DataMercuryS.objects.filter(
                date=datetime.now().strftime("%Y-%m-%d")).order_by(
                'id')
        elif name_res == 'Южный':
            return DataMercuryU.objects.filter(
                date=datetime.now().strftime("%Y-%m-%d")).order_by(
                'id')


class Substation(View):

    @staticmethod
    def add_substation(request):
        if request.method == 'POST':
            form = AddSubstation(request.POST)
            if form.is_valid():
                MercuryTCP_IP.get_model_substation(name_res=request.user.groups.all()[0]).objects.create(
                    name=form.cleaned_data['name'])
                return HttpResponseRedirect(f'http://127.0.0.1:8000/res/addTcp/')
        else:
            form = AddSubstation()
            return form

    @staticmethod
    def edit_substation(request, id_substation):
        if request.method == 'POST':
            form = EditSubstation(request.POST)
            if form.is_valid():
                new_name = form.cleaned_data['name']
                MercuryTCP_IP.get_model_substation(request.user.groups.all()[0]).objects.filter(
                    id=id_substation).update(name=new_name)
                return HttpResponseRedirect(f'http://127.0.0.1:8000/res/addTcp/showSubstation/{id_substation}/')
        else:
            form = EditSubstation()
            return form

    @staticmethod
    def add_device(request, id_substation):
        pass


def add_tcp(request):
    return render(request, 'tcp/addTcp.html',
                  {'menu': MercuryTCP_IP.get_model_substation(name_res=request.user.groups.all()[0]).objects.all(),
                   'form_add_substation': Substation.add_substation(request)})


def show_substation(request, id_substation):
    return render(request, 'tcp/showSubstation.html',
                  {'menu': MercuryTCP_IP.get_model_substation(name_res=request.user.groups.all()[0]).objects.all(),
                   'podstation': MercuryTCP_IP.get_model_substation(
                       name_res=request.user.groups.all()[0]).objects.filter(
                       Q(id=id_substation) | Q(parent_id=id_substation)),
                   'form_add_substation': Substation.add_substation(request), })
