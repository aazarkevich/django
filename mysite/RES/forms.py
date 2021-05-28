from django import forms


class AddSubstation(forms.Form):
    name = forms.CharField(label='Название', max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}))

class EditSubstation(forms.Form):
    name = forms.CharField(label='Название', max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}))

class AddDevice(forms.Form):
    name = forms.CharField(label='Название', max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}))
    ip = forms.GenericIPAddressField(label='Ip', max_length=15, widget=forms.TextInput(attrs={"class":"form-control"}))
    port = forms.DecimalField(label='Порт', widget=forms.TextInput(attrs={"class":"form-control"}))
    serial_number = forms.DecimalField(label='Серийный номер', widget=forms.TextInput(attrs={"class":"form-control"}))
