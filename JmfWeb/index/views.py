from django.shortcuts import render
from django.http import HttpResponse
from trabajos_realizados.models import Trabajos

# Create your views here.

def index(request):

    #ver para que me muestre los ultimos

    trabajos = Trabajos.objects.all().order_by("-updated")[:3]
    trabajos_antepenultimo = trabajos[0]
    trabajos_penultimo = trabajos[1]
    trabajos_ultimo = trabajos[2]

    #trabajos = Trabajos.objects.all()
    return render(request, "index/index.html", {"trabajos_antepenultimo" : trabajos_antepenultimo,
     "trabajos_penultimo" : trabajos_penultimo, "trabajos_ultimo" : trabajos_ultimo})

def quienes_somos(request):
    return render(request, "index/quienes_somos.html")

def nuestros_servicios(request):
    return render(request, "index/nuestros_servicios.html")



