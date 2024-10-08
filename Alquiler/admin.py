from django.contrib import admin
from .models import Actor, Alquiler, Director, Ejemplar, Pelicula, PeliculaActor, Socio
# Register your models here.

admin.site.register(Alquiler)
admin.site.register(Actor)
admin.site.register(Director)
admin.site.register(Ejemplar)
admin.site.register(Pelicula)
admin.site.register(PeliculaActor)
admin.site.register(Socio)