from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "index"),
    path('quienes_somos/', views.quienes_somos, name = 'quienes_somos'),
    path('nuestros_servicios/', views.nuestros_servicios, name = 'nuestros_servicios'),
]
