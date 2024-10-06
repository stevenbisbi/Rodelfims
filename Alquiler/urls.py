from django.urls import path
from Alquiler import views  # Asegúrate de importar tus vistas correctamente

urlpatterns = [
    path('home/', views.home, name='home'),
    # Agrega aquí más patrones de URL si es necesario
]