from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('menu/', views.MercuryTCP_IP.as_view(), name='menu'),
    path('addTcp/', views.add_tcp, name='add_tcp'),
    path('addTcp/showSubstation/<int:id_substation>/', views.show_substation, name='show_substation'),
    path('addTcp/addSubstation/', views.Substation.add_substation, name='add_substation'),
    path('addTcp/editSubstation/<int:id_substation>/', views.Substation.edit_substation, name='edit_substation')
]
