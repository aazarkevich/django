from django import forms


class FormSubstation(forms.Form):
    name = forms.CharField(label='Название', max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}))


class FormDevice(forms.Form):
    name = forms.CharField(label='Название', max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}))
    serial_number = forms.DecimalField(label='Серийный номер', widget=forms.TextInput(attrs={"class": "form-control"}))
    network_address = forms.DecimalField(label='Сетевой адрес', widget=forms.TextInput(attrs={"class": "form-control"}))
    ip = forms.GenericIPAddressField(label='Ip', max_length=15, widget=forms.TextInput(attrs={"class": "form-control"}))
    port = forms.DecimalField(label='Порт', widget=forms.TextInput(attrs={"class": "form-control"}))
