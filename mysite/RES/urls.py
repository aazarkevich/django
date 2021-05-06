from django.urls import path
from . import views

urlpatterns = [
    path('VRES/', views.vres),
    path('VRES/menu', views.menu, name='menu')
]
