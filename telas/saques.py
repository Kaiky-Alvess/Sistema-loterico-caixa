import tkinter as tk
from componentes.botoes import botao_padrao

def criar_tela_saque(janela, mostrar_tela, telas):
    frame = tk.Frame(janela)

    texto = tk.Label(
        frame,
        text="Digite o valor\nMin: 5,00 | Max: 5.000,00",
        font=("Arial", 12, "bold")
    )
    texto.place(relx=0.45, rely=0.42)

    entrada = tk.Entry(frame, font=("Arial", 16))
    entrada.place(relx=0.45, rely=0.5)

    botao_padrao(
        frame, "Cancelar",
        lambda: mostrar_tela(telas["principal"]),
        0.01, 0.9, "red", 12
    )

    botao_padrao(
        frame, "Confirmar",
        lambda: print("Saque:", entrada.get()),
        0.82, 0.9, "green", 12
    )

    return frame