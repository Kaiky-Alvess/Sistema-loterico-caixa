import tkinter as tk
from componentes.botoes import botao_padrao

def criar_tela_servicos(janela, mostrar_tela, telas):
    frame = tk.Frame(janela)

    botao_padrao(
        frame, "Saque",
        lambda: mostrar_tela(telas["saque"]),
        0.01, 0.25
    )

    botao_padrao(
        frame, "Depósito",
        lambda: print("Depósito"),
        0.2, 0.25
    )

    botao_padrao(
        frame, "Voltar",
        lambda: mostrar_tela(telas["principal"]),
        0.01, 0.9, "gray", 10
    )

    return frame