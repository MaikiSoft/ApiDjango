from django.shortcuts import render
from inventario.api import ConsumirApi
# Create your views here.

def inicio(request):
    context = ConsumirApi(request)
    return render(request, "inventario/index.html", context)
    
