from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index),
    path('autorization/', views.Autorization.as_view(), name='autorization'),
    path('logout/',views.Autorization.as_view()),
    # re_path(r'(.RES)/login/logout/', views.Autorization.as_view()),
]
