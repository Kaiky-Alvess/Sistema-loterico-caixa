import tkinter as tk

from telas.principal import criar_tela_principal
from telas.resultados import criar_tela_resultados
from telas.serviços import criar_tela_servicos
from telas.saques import criar_tela_saque

def iniciar():
    janela = tk.Tk()
    janela.geometry("1920x1080")
    janela.state("zoomed")
    janela.title("Sistema Lotérico Caixa")

    tela_atual = {"frame": None}

    def mostrar_tela(frame):
        if tela_atual["frame"]:
            tela_atual["frame"].pack_forget()

        frame.pack(fill="both", expand=True)
        tela_atual["frame"] = frame

    telas = {}

    telas["principal"] = criar_tela_principal(janela, mostrar_tela, telas)
    telas["resultados"] = criar_tela_resultados(janela, mostrar_tela, telas)
    telas["servicos"] = criar_tela_servicos(janela, mostrar_tela, telas)
    telas["saque"] = criar_tela_saque(janela, mostrar_tela, telas)

    mostrar_tela(telas["principal"])

    janela.mainloop()