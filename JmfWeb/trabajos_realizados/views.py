from django.shortcuts import render
from .models import Trabajos, CategoriaTrab

# Create your views here.
def trabajos_realizados(request):
    
    trabajos = Trabajos.objects.all()
    
    # trabajoId = int(trabajos.id)

    # if trabajoId % 2 == 0:
    #     trabajoIdPar = trabajoId
    #     return trabajoIdPar
    return render(request, "trabajos_realizados/trabajos_realizados.html", {"trabajos" : trabajos})



