from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='mercury'),
    path('TcpIp/<int:id_substation>/', views.tcp_ip, name='mercuryTcp'),

]
