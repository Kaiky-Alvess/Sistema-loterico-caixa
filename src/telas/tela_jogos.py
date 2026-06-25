import tkinter as tk


def criar_tela_jogos(janela,mostrar_tela,carrinho):
    def ver_jogos():
        for widget in tela.winfo_children():
            if isinstance(widget, tk.Label):

                widget.destroy()
        pos = 0
        for i, jogo in enumerate(carrinho):
            if jogo['nome'] == 'Lotofacil' or jogo['nome'] == 'Mega Sena' or jogo['nome'] == 'Quina':
                pos += 1
                mostrar_jogos = tk.Label(tela, text=f'{jogo["nome"]} {pos}'
                                                    f'\n {jogo["numeros"]}',
                                         font=('Arial', 20, 'bold'))

                mostrar_jogos.pack()
        mostrar_tela("atendimento")
    tela = tk.Frame(janela)

    botao_voltar = tk.Button(tela, text='Voltar', font=('Arial', 30, 'bold'), command=lambda:mostrar_tela("atendimento"),
                             bd=2, relief="solid")
    botao_voltar.place(relx=0.01, rely=0.9)

    return tela,ver_jogos
