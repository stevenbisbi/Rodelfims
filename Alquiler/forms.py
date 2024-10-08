from .models import Actor, Alquiler, Director, Ejemplar, Pelicula, PeliculaActor, Socio
from django import forms

class SocioForm(forms.ModelForm):
    class Meta:
        model = Socio
        fields= ['dni', 'nombre', 'direccion', 'telefono', 'avalado_por']
        widgets = {
            'dni': forms.NumberInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'tefelono': forms.NumberInput(attrs={'class': 'form-control'}),
            'avalado_por': forms.Select(attrs={'class': 'form-control'}),
        }
        
class DirectorForm(forms.ModelForm):
    model = Director
    fields= ['nombre', 'nacionalidad']
    widgets={
        'nombre': forms.TextInput(attrs={'class': 'form-control'}),
        'nacionalidad': forms.TextInput(attrs={'class': 'form-control'}),
    }

class AlquilerForms(forms.ModelForm):
    model = Alquiler
    fields= ['fecha_comienzo', 'fecha_devolucion', 'id_ejemplar', 'dni_socio']
    widgetis = {
        'fecha_comienzao': forms.DateInput(attrs={'class': 'form-control'}),
        'fecha_devolucion': forms.DateInput(attrs={'class': 'form-control'}),
        'id_ejemplar': forms.Select(attrs={'class': 'form-control'}),
        'dni_socio': forms.Select(attrs={'class': 'form-control'}),  
    }
    
class EjemplarForm(forms.ModelForm):
    model = Ejemplar
    fields = ['estado_conservacion', 'id_pelicula']
    widgets = {
        'estado_conservacion': None,
        'id_pelicula': forms.Select(attrs={'class': 'form-control'})
    }
    
class ActorForm(forms.ModelForm):
    model = Actor
    fields = ['nombre', 'nacionalidad', 'sexo']
    widgets = {
        'nombre': forms.TextInput(attrs={'class': 'form-control'}),
        'nacionalidad': forms.TextInput(attrs={'class': 'form-control'}),
        'sexo': forms.TextInput(attrs={'class': 'form-control'})
    }
    
class PeliculaForm(forms.ModelForm):
    model = Pelicula
    fields = ['titulo', 'nacionalidad', 'productora', 'fecha', 'id_director']
    widgets = {
        'titulo': forms.TextInput(attrs={'class': 'form-control'}),
        'nacionalidad': forms.TextInput(attrs={'class': 'form-control'}),
        'productora': forms.TextInput(attrs={'class': 'form-control'}),
        'fecha': forms.DateInput(attrs={'class': 'form-control'}),
        'id_director': forms.Select(attrs={'class': 'form-control'}),
        
    }