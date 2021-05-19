from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('menu/', views.MercuryTCP_IP.as_view(), name='menu'),
    path('addTcp/', views.add_tcp, name='add_tcp')
]
