from django.http import HttpResponse
from appcoder.models import Curso
from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request, "appcoder/index.html")

def cursos(request):
    return HttpResponse("Estas en Cursos")

def estudiantes(request):
    return HttpResponse("Estas en Estudiantes")

def profesores(request):
    return HttpResponse("Estas en Profesores")

def entregables(request):
    return HttpResponse("Estas en Entrehables")
