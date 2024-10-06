from django.db import models

# Create your models here.

class Director(models.Model):
    id_director = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
    
class Actor(models.Model):
    id_actor = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=50)
    sexo = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre

class Pelicula(models.Model):
    id_pelicula = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=50)
    productora = models.CharField(max_length=100, null=True, blank=True)
    fecha = models.DateField()
    id_director = models.ForeignKey(Director, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.titulo

class PeliculaActor(models.Model):
    id_pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)
    id_actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    principal = models.BooleanField(default=False)

    class Meta:
        unique_together = ('id_pelicula', 'id_actor')

class Ejemplar(models.Model):
    id_ejemplar = models.AutoField(primary_key=True)
    estado_conservacion = models.CharField(max_length=50)
    id_pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)

    def __str__(self):
        return f"Ejemplar de {self.id_pelicula.titulo}"

class Socio(models.Model):
    dni = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200, null=True, blank=True)
    telefono = models.IntegerField(null=True, blank=True)
    avalado_por = models.ForeignKey('Socio', null=True, blank=True, on_delete=models.SET_NULL, related_name='avaladores')

    def __str__(self):
        return self.nombre

class Alquiler(models.Model):
    id_alquiler = models.AutoField(primary_key=True)
    fecha_comienzo = models.DateField()
    fecha_devolucion = models.DateField(null=True, blank=True)
    id_ejemplar = models.ForeignKey(Ejemplar, on_delete=models.CASCADE)
    dni_socio = models.ForeignKey(Socio, on_delete=models.CASCADE)

    def __str__(self):
        return f"Alquiler {self.id_alquiler} - {self.dni_socio.nombre}"

