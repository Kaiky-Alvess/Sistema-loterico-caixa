import tkinter as tk

def criar_tela_conta_criada(janela,mostrar_tela):

    tela=tk.Frame(janela)
    informacoes = tk.Label(tela, font=('Arial', 25, 'bold'), )
    informacoes.place(relx=0.01, rely=0.1)

    botao_voltar = tk.Button(tela, text='Voltar', font=('Arial', 30, 'bold'),
                             command=lambda: mostrar_tela("principal"))
    botao_voltar.place(relx=0.01, rely=0.9)
    return tela,informacoes