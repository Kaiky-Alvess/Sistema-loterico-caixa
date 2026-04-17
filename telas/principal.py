import tkinter as tk
from componentes.botoes import botao_padrao
from loterias.loterias import criar_tela_loteria

def criar_tela_principal(janela, mostrar_tela, telas):
    frame = tk.Frame(janela)

    mega = criar_tela_loteria(
        janela,
        lambda: mostrar_tela(frame),
        "Mega Sena", 60, 6, 10, "green", "#DAA520"
    )

    loto = criar_tela_loteria(
        janela,
        lambda: mostrar_tela(frame),
        "Lotofácil", 25, 15, 5, "purple", "#DAA520"
    )

    quina = criar_tela_loteria(
        janela,
        lambda: mostrar_tela(frame),
        "Quina", 80, 5, 10, "blue", "#DAA520"
    )

    botao_padrao(frame, "Serviços Financeiros",
                 lambda: mostrar_tela(telas["servicos"]), 0.01, 0.2)

    botao_padrao(frame, "Últimos Resultados",
                 lambda: mostrar_tela(telas["resultados"]), 0.25, 0.2)

    botao_padrao(frame, "MEGA SENA",
                 lambda: [mega.limpar_aposta(), mostrar_tela(mega)],
                 0.7, 0.2, "green")

    botao_padrao(frame, "LOTOFÁCIL",
                 lambda: [loto.limpar_aposta(), mostrar_tela(loto)],
                 0.7, 0.3, "purple")

    botao_padrao(frame, "QUINA",
                 lambda: [quina.limpar_aposta(), mostrar_tela(quina)],
                 0.7, 0.4, "blue")

    return frame