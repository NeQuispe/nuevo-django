from django.shortcuts import render
# from django.template import loader
# from django.http import HttpResponse
from Index.models import Paleta
# Create your views here.


def index(request):
    # V2
    # template = loader.get_template("index.html")
    # template_renderizado = template.render({})
    
    # return HttpResponse(template_renderizado)
    
    # V3
    return render(request, "Index/index.html", {})

def paletas(request):
    
    paleta = Paleta(marca="Wilson", descripcion= "Paleta de tenis", anio=2023)
    paleta.save()
    
    return render(request, "Index/paletas.html", {"paleta":paleta})