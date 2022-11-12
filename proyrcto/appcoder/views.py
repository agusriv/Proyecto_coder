from django.http import HttpResponse
from appcoder.models import Curso, Profesor
from appcoder.forms import ProfesorFormulario
from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request, "appcoder/index.html")

def cursos(request):
    return render(request, "appcoder/cursos.html")

def estudiantes(request):
    return render(request, "appcoder/estudiantes.html")

def profesores(request):
    return render(request, "appcoder/profesores.html")

def creacion_profesores(request):

    if request.method == "POST":
        formulario = ProfesorFormulario(request.POST)
        # Validamos que el formulario no tenga problemas
        if formulario.is_valid():
            # Recuperamos los datos del atributo cleaned_data
            data = formulario.cleaned_data
            profesor = Profesor(nombre=data["nombre"], apellido=data["apellido"], email=data["email"],
            profesion = data["profesion"])

            profesor.save()

    formulario = ProfesorFormulario()
    return render(request, "appcoder/profesores_formularios.html", {"formulario": formulario})

def entregables(request):
    return render(request, "appcoder/entregables.html")

def creacion_curso(request):

    if request.method == "POST":
        nombre_curso = request.POST["curso"]
        numero_camada = request.POST["camada"]

        curso = Curso(nombre=nombre_curso, camada=numero_camada)
        curso.save()

    return render(request, "appcoder/curso_formulario.html")