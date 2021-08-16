from django.urls import path
from . import views
from datetime import datetime

urlpatterns = [
    path('', views.index),
    path('menu/<slug:date>', views.MercuryTCP_IP.as_view(), name='menu'),
    path('addTcp/', views.add_tcp, name='add_tcp'),
    path('addTcp/showSubstation/<int:id_substation>/', views.show_substation, name='show_substation'),
    path('addTcp/addSubstation/', views.Substation.add_substation, name='add_substation'),
    path('addTcp/editSubstation/<int:id_substation>/', views.Substation.edit_substation, name='edit_substation'),
    path('addTcp/deleteSubstation/<int:id_substation>/', views.Substation.delete_substation, name='delete_substation'),
    path('addTcp/addDevice/<int:id_substation>/', views.Substation.add_device, name='add_device'),
    path('addTcp/deleteDevice/<int:id_device>/', views.Substation.delete_device, name='delete_device'),
    path('addTcp/editDevice/<int:id_node_device>/', views.Substation.edit_device, name='edit_device'),
]
