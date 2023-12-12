from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader

def saludo(request):
    return HttpResponse("Exportagro Argentina Comex")

def probandoTemplate(request):

    nombre = "Tamara"
    apellido = "Martinez"
    diccionario = {"nombre": nombre, "apellido": apellido}
    plantilla = loader.get_template("plantilla1.html")
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)