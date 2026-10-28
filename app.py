import json
import requests
from modulos import clima
def test_clemate():
    try:
        dados = clima.climate_search()
        print(f"Agora: {dados['temperature']} ºC ")
        print(f"Hoje: {dados['min']} a {dados['max']} ºC")
        print(f"Previsão de chuva: {dados['precepitation']}%")
    except requests.RequestException as erro:
        print(f'Sem conexão ou API fora do ar: {erro}')
    except KeyError as erro:
        print(f'API não contêm a chave esperada: {erro}')

def main():
    print("SANTIAGO - RS")

    test_clemate()

if __name__ == "__main__":
    main()