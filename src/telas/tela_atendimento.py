import tkinter as tk


def criar_tela_atendimento(janela, mostrar_tela,carrinho,abrir_tela_confirmar):
    def calcular_carrinho():
        total = sum(item["preco"] for item in carrinho)
        label_total.config(text=f"Total: R$ {total:.2f}")

    def finalizar_atendimento():
        carrinho.clear()
        atualizar_carrinho()
        calcular_carrinho()
        mostrar_tela("principal")

    def atualizar_carrinho():
        for widget in frame_lista.winfo_children():
            widget.destroy()
        for i, item in enumerate(carrinho):
            linha = tk.Frame(frame_lista)
            linha.pack(fill="x", pady=5, padx=10)
            if item["preco"] < 0:
                texto = tk.Label(linha, text=f'{item["nome"]} |  R${item["preco"] * -1:.2f}', font=("Arial", 16),
                                 anchor="w")
                texto.pack(side="left")
            else:
                texto = tk.Label(linha, text=f'{item["nome"]} |  R${item["preco"]:.2f}', font=("Arial", 16), anchor="w")
                texto.pack(side="left")
            if not item["nome"] == "Saque":
                botao_remover = tk.Button(linha, text="—", font=("Arial", 14, "bold")
                                          , bg="red", fg="white", command=lambda idx=i: remover_aposta(idx))
                botao_remover.pack(side="left")
            calcular_carrinho()

    def remover_aposta(indice):
        carrinho.pop(indice)
        atualizar_carrinho()
        calcular_carrinho()

    tela = tk.Frame(janela)

    texto = tk.Label(tela, font=("Arial", 16))
    texto.pack()

    label_total = tk.Label(tela, font=("Arial", 18, "bold"))
    label_total.pack()

    frame_lista = tk.Frame(tela)
    frame_lista.pack(pady=20, fill="both", expand=True)

    botao_ver_jogos = tk.Button(tela, text='Ver Jogos', font=('Arial', 30, 'bold'),
                                bd=2, relief="solid",
                                command=lambda: mostrar_tela("jogos"))
    botao_ver_jogos.place(relx=0.5, rely=0.9, anchor='center')

    botao_finalizar = tk.Button(tela, text='Finalizar', font=('Arial', 30, 'bold'),
                                command=abrir_tela_confirmar
                                , bd=2, relief="solid")
    botao_finalizar.place(relx=0.89, rely=0.9)

    botao_voltar = tk.Button(tela, text='Voltar', font=('Arial', 30, 'bold'),
                             command=lambda:mostrar_tela("principal"), bd=2, relief="solid")
    botao_voltar.place(relx=0.01, rely=0.9)
    return tela,atualizar_carrinho