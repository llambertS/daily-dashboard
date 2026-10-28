import requests
from modulos import clima

try:
    dados = clima.climate_search()
    print(f"Agora: {dados['temperatura']} ºC ")
    print(f"Hoje: {dados['minima']} a {dados['maxima']} ºC")
except requests.RequestException as erro:
    print(f'Sem conexão ou API fora do ar: {erro}')
except KeyError as erro:
    print(f'API não contêm a chave esperada: {erro}')
