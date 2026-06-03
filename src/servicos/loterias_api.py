import requests
def buscar_lotofacil(texto):
    url = "https://loteriascaixa-api.herokuapp.com/api/lotofacil/latest"
    resposta = requests.get(url)
    dados = resposta.json()
    numeros = dados["dezenas"]
    concurso = dados["concurso"]
    texto.config(text=f"Lotofácil\nConcurso {concurso}\n" + " - ".join(numeros),
                           bg="purple", fg="white")

def buscar_megasena(texto):
    url = f"https://loteriascaixa-api.herokuapp.com/api/megasena/latest"
    resposta = requests.get(url)
    dados = resposta.json()
    numeros = dados["dezenas"]
    concurso = dados["concurso"]
    texto.config(text=f"Mega Sena\nConcurso {concurso}\n" + " - ".join(numeros),
                           bg="green",fg="white")

def buscar_quina(texto):
    url="https://loteriascaixa-api.herokuapp.com/api/quina/latest"
    resposta= requests.get(url)
    dados = resposta.json()
    numeros = dados["dezenas"]
    concurso = dados["concurso"]
    texto.config(text=f"Quina\nConcurso {concurso}\n" + " - ".join(numeros),
                           bg="blue",fg="white")