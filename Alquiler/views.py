from django.shortcuts import render, HttpResponse
from .models import Actor
# Create your views here.
def home(request):
    actores = Actor.objects.all()
    return render(request, 'home.html', {'actores': actores})

def alquiler(request):
    return render(request, 'alquiler.html')

def singin(request):
    return render(request, 'singin.html')