from .models import Actor, Alquiler, Director, Ejemplar, Pelicula, PeliculaActor, Socio
from django import forms

class SocioForm(forms.ModelForm):
    class Meta:
        model = Socio
        fields= ['']