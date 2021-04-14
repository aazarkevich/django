from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def mercury_tcp(request):
    return render(request, 'main/mercury_tcp.html')

def mercury_gsm(request):
    return render(request, 'main/mercury_gsm.html')