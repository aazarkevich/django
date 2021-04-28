from django.urls import path
from . import views


urlpatterns = [
    path('', views.vres, name = 'vres'),
]
