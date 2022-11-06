from pipes import Template
from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader

def vista_saludo(request):
    return HttpResponse("Hola mundo! :)")

def iniciar_secion(request):
    return HttpResponse("Pasame tu username y tu password")

def dia_hoy(request, nombre):
    return HttpResponse("hola {}, hoy es: {}".format(nombre, datetime.now()))

def año_nacimiento(request, edad):
    edad = int(edad)
    año_nac = datetime.now().year - edad
    return HttpResponse("Naciste en el año {}".format(año_nac))

def vista_plantilla(request):
    archivo = open(r"C:\Users\agustin\OneDrive\Escritorio\Django\proyrcto\proyrcto\templates\plantilla.html")

    plantilla = Template(archivo.read())

    archivo.close

    datos= {"nombre":"Agustín", "apellido":"Rivera", "fecha": datetime.now()}

    contexto = Context(datos)

    documento = plantilla.render(contexto)

    return HttpResponse(documento)

def vista_listado_alumnos(request):
    archivo = open(r"C:\Users\agustin\OneDrive\Escritorio\Django\proyrcto\proyrcto\templates\listado_alumnos.html")

    plantilla = Template(archivo.read())

    archivo.close()

    lista_alumnos = ["Agustin Rivera", "Lautaro Rivera"]

    datos = {"listado_alumnos": lista_alumnos, "tecnologia":"Python"}

    contexto = Context(datos)

    documento = plantilla.render(contexto)

    return HttpResponse(documento)

def vista_listado_alumnos2(request):
    # Creamos el diccionario de datos
    listado_alumnos = ["Leonel Gareis", "Agustin Russo", 
    "Cristian Garcia", "Angelo Pettinari", "Diego Ibarra", "Santiago Ortiz", "Barbara Vivante",  "Barbara Pino"]
    datos = {"tecnologia": "Python", "listado_alumnos": listado_alumnos}

    plantilla = loader.get_template("listado_alumnos.html")
    documento = plantilla.render(datos)
    
    return HttpResponse(documento)



