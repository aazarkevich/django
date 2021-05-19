from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .models import TreeMenuV, DataMercuryV, TreeMenuZ, DataMercuryZ
from django.views.generic import View


def index(request):
    return render(request, 'base.html', {'name_res': request.user.groups.all()[0]})


class MercuryTCP_IP(View):

    def get(self, request):
        return render(request, 'tcp/menu.html', {'menu': self.menu(name_res=request.user.groups.all()[0]),
                                                 'values': self.values_tp(name_res=request.user.groups.all()[0])})
    @staticmethod
    def menu(name_res):
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


def add_tcp(request):

    return render(request, 'tcp/addTcp.html', {'menu': MercuryTCP_IP.menu(name_res=request.user.groups.all()[0])})
