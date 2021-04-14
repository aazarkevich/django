from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about', views.about),
    path('mercury_tcp', views.mercury_tcp, name='mercury_tcp'),
    path('mercury_gsm', views.mercury_gsm, name='mercury_gsm')
]
