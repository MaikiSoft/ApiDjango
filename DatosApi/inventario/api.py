from urllib.request import urlopen
import json
import urllib.parse  # Importa el módulo para codificar la URL

def ConsumirApi():
    base_url = "https://gateway.marvel.com:443/v1/public/characters"
    params = {
        "name": "Hulk",
        "apikey": "07ae1840831537496180cbbe6a6fc3dd",
        "hash": "9956ccc80ee4192f80b9e91d6797ba69",
        "ts": "1"
    }
    # Codifica los parámetros de la URL
    encoded_params = urllib.parse.urlencode(params)
    url = f"{base_url}?{encoded_params}"

    try:
        response = urlopen(url)
        data = json.loads(response.read())
        return data
    except Exception as e:
        return print(f"Error al hacer la solicitud: {e}")

ConsumirApi()