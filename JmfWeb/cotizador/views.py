from django.shortcuts import render

# Create your views here.
def cotizador(request):
    return render(request, 'cotizador/cotizador.html')