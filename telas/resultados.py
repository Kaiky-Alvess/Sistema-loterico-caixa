import tkinter as tk
from componentes.botoes import botao_padrao
from utilidades.api import buscar_resultado

def criar_tela_resultados(janela, mostrar_tela, telas):
    frame = tk.Frame(janela)

    texto_resultado = tk.Label(
        frame,
        font=("Arial", 20, "bold"),
        justify="center"
    )
    texto_resultado.place(relx=0.48, rely=0.5, anchor="center")

    def mostrar(nome, titulo, cor):
        concurso, numeros = buscar_resultado(nome)

        texto_resultado.config(
            text=f"{titulo}\nConcurso {concurso}\n" + " - ".join(numeros),
            bg=cor,
            fg="white"
        )

    botao_padrao(
        frame, "MEGA SENA",
        lambda: mostrar("megasena", "Mega Sena", "green"),
        0.2, 0.2, "green", 10
    )

    botao_padrao(
        frame, "LOTOFÁCIL",
        lambda: mostrar("lotofacil", "Lotofácil", "purple"),
        0.4, 0.2, "purple", 10
    )

    botao_padrao(
        frame, "QUINA",
        lambda: mostrar("quina", "Quina", "blue"),
        0.6, 0.2, "blue", 10
    )

    botao_padrao(
        frame, "Voltar",
        lambda: mostrar_tela(telas["principal"]),
        0.01, 0.9, "gray", 10
    )

    return frame