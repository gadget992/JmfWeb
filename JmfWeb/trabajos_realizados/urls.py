from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.trabajos_realizados, name = 'trabajos_realizados'),
]
