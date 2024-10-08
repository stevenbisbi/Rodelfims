from django.urls import path
from Alquiler import views  # Asegúrate de importar tus vistas correctamente

urlpatterns = [
    path('home/', views.home, name='home'),
    path('alquiler/', views.alquiler, name='alquiler'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
]