import requests

def buscar_resultado(nome):
    url = f"https://loteriascaixa-api.herokuapp.com/api/{nome}/latest"
    dados = requests.get(url).json()
    return dados["concurso"], dados["dezenas"]