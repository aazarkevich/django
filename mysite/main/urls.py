from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('mercury_gsm/', views.mercury_gsm, name='mercury_gsm'),
    path('VRES/', views.vres, name='VRES')
]
