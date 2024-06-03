from django.shortcuts import render
from django.http import HttpResponse
from .models import Proyecto

from django.contrib.auth import authenticate,login,logout

# Create your views here.
def home (request):    

    return render (request, 'core/onepage.html')

def sesion (request):

    return render (request, 'core/onepage.html')

def proyectos(request):
    titulo = "Proyectos weeeeh!!!"

    lista_proyectos = Proyecto.objects.all()

    data = {
        "titulo" : titulo,
        "lista_proyectos" : lista_proyectos,
    }
    return render (request,'core/onepage.html', data)
