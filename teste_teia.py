import requests
import json

url = 'https://render.com/docs/web-services#port-detection'
data = {'texto': 'banana'}

try:
    response = requests.post(url, json=data)
    response_json = response.json()
except json.JSONDecodeError:
    print('Erro ao decodificar JSON. A resposta não é válida')


print(response.json())