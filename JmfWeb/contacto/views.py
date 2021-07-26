from django.shortcuts import render, redirect
from .forms import FormularioContacto
from django.core.mail import EmailMessage

# Create your views here.

def contacto(request):
    formulario = FormularioContacto()

    if request.method == 'POST':
        formulario_contacto = FormularioContacto(data = request.POST)

        if formulario_contacto.is_valid():
            nombre = request.POST.get("nombre")
            email = request.POST.get("email")
            consulta = request.POST.get("consulta")

            #para el email que llega
            email = EmailMessage("mensaje desde app django",
            "el usuario con nombre {}, con la direccion {}, escribe lo siguiente: \n \n {}".format(nombre, email, consulta),
            "", ["martin.orteguita2020@gmail.com"], reply_to = [email])

            try:
                email.send()
                return redirect('/contacto/?valido')
            
            except:
                return redirect('/contacto/?novalido')
                
    return render(request, 'contacto/contacto.html', {'formulario': formulario})