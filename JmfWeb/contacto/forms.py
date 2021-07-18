from django import forms

class FormularioContacto(forms.Form):
    nombre = forms.CharField(label = 'Nombre', required = True, widget=forms.TextInput(attrs={'placeholder': '¿Como te llamas?'}))
    email = forms.CharField(label = 'Email: ', required = True)
    consulta = forms.CharField(label = 'Consulta: ', widget = forms.Textarea(attrs={'style' : 'width: 100%; height:100px'}))
