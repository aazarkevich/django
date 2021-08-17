from RES.views import MercuryTCP_IP
from django.db.models import Q
from django.shortcuts import render
from django.views.generic import View
from datetime import datetime

from .mercury_device.mercuryTCP import MercuryTCP


def index(request):
    return render(request, 'mercury/podstations.html',
                  {'menu': MercuryTCP_IP.get_model_substation(name_res=request.user.groups.all()[0]).objects.all(),
                   'date': datetime.now().strftime("%Y-%m-%d")})

class SubstationValues(View):
    def get(self, request, id_substation):
        node_devices = MercuryTCP_IP.get_model_substation(request.user.groups.all()[0]).objects.filter(
            parent_id=id_substation)
        values = dict()
        for device in node_devices:
            mercury = MercuryTCP(serial_number=device.device.serial_number, ip=device.device.ip,
                                 port=device.device.port, network_address=device.device.network_address)
            values[device.device.serial_number] = mercury.get_values()

        return self.show_substation_values(request, id_substation, values=values)

    @staticmethod
    def show_substation_values(request, id_substation, values=None):
        return render(request, 'mercury/tcpIp.html',
                      {'menu': MercuryTCP_IP.get_model_substation(name_res=request.user.groups.all()[0]).objects.all(),
                       'podstation': MercuryTCP_IP.get_model_substation(
                           name_res=request.user.groups.all()[0]).objects.filter(
                           Q(id=id_substation) | Q(parent_id=id_substation)),
                       'values': values,
                       'date': datetime.now().strftime("%Y-%m-%d")
                       })
