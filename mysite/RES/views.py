from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime
from .models import *
from django.views.generic import View
from django.db.models import Q
from .forms import FormSubstation, FormDevice


def index(request):
    return render(request, 'base.html',
                  {'name_res': request.user.groups.all()[0], 'date': datetime.now().strftime("%Y-%m-%d")})


class MercuryTCP_IP(View):

    def get(self, request, date=datetime.now().strftime("%Y-%m-%d")):
        substations = MercuryTCP_IP.get_model_substation(name_res=request.user.groups.all()[0]).objects.filter(
            parent_id=None)

        return render(request, 'tcp/menu.html',
                      {'menu': self.get_model_substation(name_res=request.user.groups.all()[0]).objects.all(),
                       'values': self.values_tp(name_res=request.user.groups.all()[0]).objects.filter(
                           date=date).order_by(
                           'id'),
                       'substations': substations,
                       'date': datetime.now().strftime("%Y-%m-%d")})

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

    @staticmethod
    def get_model_device(name_res):
        name_res = str(name_res)
        if name_res == 'Восточный':
            return DeviceMercuryV
        elif name_res == 'Западный':
            return DeviceMercuryZ
        elif name_res == 'Северный':
            return DeviceMercuryS
        elif name_res == 'Южный':
            return DeviceMercuryU

    @staticmethod
    def values_tp(name_res):
        name_res = str(name_res)
        if name_res == 'Восточный':
            return DataMercuryV
        elif name_res == 'Западный':
            return DataMercuryZ
        elif name_res == 'Северный':
            return DataMercuryS
        elif name_res == 'Южный':
            return DataMercuryU


class Substation(View):

    @staticmethod
    def add_substation(request):
        if request.method == 'POST':
            form = FormSubstation(request.POST)
            if form.is_valid():
                new_substation = MercuryTCP_IP.get_model_substation(
                    name_res=request.user.groups.all()[0]).objects.create(
                    name=form.cleaned_data['name'])

                return HttpResponseRedirect(f'/res/addTcp/showSubstation/{new_substation.id}')
        else:
            form = FormSubstation()
            return form

    @staticmethod
    def edit_substation(request, id_substation):
        if request.method == 'POST':
            name = FormSubstation(request.POST)
            form = request.POST
            if name.is_valid():
                new_name = name.cleaned_data['name']
                new_ip = form['ip']
                new_port = form['port']

                node_devices = MercuryTCP_IP.get_model_substation(request.user.groups.all()[0]).objects.filter(
                    parent_id=id_substation)
                for device in node_devices:
                    MercuryTCP_IP.get_model_device(request.user.groups.all()[0]).objects.filter(
                        id=device.device.id).update(ip=new_ip, port=new_port)

                MercuryTCP_IP.get_model_substation(request.user.groups.all()[0]).objects.filter(
                    id=id_substation).update(name=new_name)
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            form = FormSubstation()
            return form

    @staticmethod
    def delete_substation(request, id_substation):
        MercuryTCP_IP.get_model_substation(request.user.groups.all()[0]).objects.filter(id=id_substation).delete()
        return HttpResponseRedirect('/res/addTcp/')

    @staticmethod
    def add_device(request, id_substation):

        if request.method == 'POST':
            form = FormDevice(request.POST)
            if form.is_valid():
                name_node_values = form.cleaned_data['name']
                device_ip = form.cleaned_data['ip']
                device_port = form.cleaned_data['port']
                device_serial_number = form.cleaned_data['serial_number']
                device_network_adress = form.cleaned_data['network_address']

                device = MercuryTCP_IP.get_model_device(request.user.groups.all()[0]).objects.create(ip=device_ip,
                                                                                                     port=device_port,
                                                                                                     serial_number=device_serial_number,
                                                                                                     network_address=device_network_adress)
                substation = MercuryTCP_IP.get_model_substation(request.user.groups.all()[0]).objects.get(
                    id=id_substation)
                MercuryTCP_IP.get_model_substation(request.user.groups.all()[0]).objects.create(
                    name=name_node_values, parent=substation, device=device)

                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            node_device = MercuryTCP_IP.get_model_substation(request.user.groups.all()[0]).objects.filter(
                parent_id=id_substation)
            if node_device:
                device = MercuryTCP_IP.get_model_substation(request.user.groups.all()[0]).objects.filter(
                    parent_id=id_substation).first().device
                form = FormDevice(initial={'ip': device.ip, 'port': device.port})
                form.fields['ip'].widget.attrs['readonly'] = True
                form.fields['port'].widget.attrs['readonly'] = True
                return form

            form = FormDevice()

            return form

    @staticmethod
    def delete_device(request, id_device):
        for data in MercuryTCP_IP.values_tp(request.user.groups.all()[0]).objects.filter(id_tp=id_device):
            data.delete()
        MercuryTCP_IP.get_model_substation(request.user.groups.all()[0]).objects.get(id=id_device).device.delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    @staticmethod
    def edit_device(request, id_node_device):

        if request.method == 'POST':
            form = FormDevice(request.POST)
            if form.is_valid():
                node_device = MercuryTCP_IP.get_model_substation(request.user.groups.all()[0]).objects.filter(
                    id=id_node_device)

                device = MercuryTCP_IP.get_model_device(request.user.groups.all()[0]).objects.filter(
                    id=node_device.get().device.id)

                device.update(serial_number=form.cleaned_data['serial_number'],
                              network_address=form.cleaned_data['network_address'])
                node_device.update(name=form.cleaned_data['name'])

                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            node_device = MercuryTCP_IP.get_model_substation(request.user.groups.all()[0]).objects.filter(
                parent_id=id_node_device).first()
            if node_device:
                device = MercuryTCP_IP.get_model_substation(request.user.groups.all()[0]).objects.filter(
                    parent_id=id_node_device).first().device
                form = FormDevice(initial={'ip': device.ip, 'port': device.port})
                form.fields['ip'].widget.attrs['readonly'] = True
                form.fields['port'].widget.attrs['readonly'] = True
                return form

            form = FormDevice()
            return form


def add_tcp(request):
    return render(request, 'tcp/tcp.html',
                  {'menu': MercuryTCP_IP.get_model_substation(name_res=request.user.groups.all()[0]).objects.all(),
                   'form_substation': Substation.add_substation(request),
                   'date': datetime.now().strftime("%Y-%m-%d")})


def show_substation(request, id_substation):
    return render(request, 'tcp/showSubstation.html',
                  {'menu': MercuryTCP_IP.get_model_substation(name_res=request.user.groups.all()[0]).objects.all(),
                   'podstation': MercuryTCP_IP.get_model_substation(
                       name_res=request.user.groups.all()[0]).objects.filter(
                       Q(id=id_substation) | Q(parent_id=id_substation)),
                   'form_substation': Substation.add_substation(request),
                   'form_device': Substation.edit_device(request, id_substation),
                   'date': datetime.now().strftime("%Y-%m-%d")})
