from django.urls import path
from appcoder.views import *

urlpatterns =[
    path("estudiantes/", estudiantes, name= "coder-estudiantes"),
    path("profesores/", profesores, name= "coder-profesores"),
    path("profesores/crear/", creacion_profesores, name= "coder-profesores-crear"),
    path("cursos/", cursos, name= "coder-cursos"),
    path("cursos/crear/", creacion_curso, name="coder-cursos-crear"),
    path("entregables/", entregables, name= "coder-entregables"),
    path("inicio/", inicio, name= "coder-inicio"),
    path("cursos/buscar/", buscar_curso, name= "coder-cursos-buscar"),
    path("cursos/buscar/resultados/", resultado_busqueda_curso, name= "coder-cursos-buscar-resultados")

]