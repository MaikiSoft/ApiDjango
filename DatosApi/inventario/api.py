from urllib.request import urlopen
import json
from django.http import JsonResponse  # Importa JsonResponse para devolver datos JSON

def ConsumirApi(request):
    url = "https://api.covidtracking.com/v2/states/ca/2021-01-10.json"

    try:
        response = urlopen(url)
        data = json.loads(response.read())
        return data  # Devuelve los datos como un diccionario
    except Exception as e:
        return {"error": f"Error al hacer la solicitud: {e}"}