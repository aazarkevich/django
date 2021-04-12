from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h4>Hello world</h4>')
# Create your views here.
def about(request):
    return HttpResponse('<h4>HelLo Artemka</h4>')