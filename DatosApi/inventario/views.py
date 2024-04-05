from django.shortcuts import render
from inventario.api import ConsumirApi
# Create your views here.

def inicio(request):
    try:
        render(request,"invenatio/index.html", ConsumirApi)
    except Exception as e:
        render(request,"inventario/index.html")
    
