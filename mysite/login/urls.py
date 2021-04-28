from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('autorization/', views.Autorization.as_view(), name='autorization'),
    path('logout/', views.Autorization.as_view()),
]
