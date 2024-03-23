import requests
import json

url = 'http://localhost:5000/analyze_string'
data = {'texto': 'banana'}

try:
    response = requests.post(url, json=data)
    response_json = response.json()
except json.JSONDecodeError:
    print('Erro ao decodificar JSON. A resposta não é válida')


print(response.json())