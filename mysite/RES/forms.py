from django import forms


class AddSubstation(forms.Form):
    name = forms.CharField(label='Название', max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}))
