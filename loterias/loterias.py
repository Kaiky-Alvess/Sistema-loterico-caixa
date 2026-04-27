import tkinter as tk
from random import randint

def criar_tela_loteria(janela,funcao_voltar, titulo,total_numeros,limite,colunas,cor_fundo,cor_marcado,carrinho,preco):
    selecionados = []
    botoes = []
    apostas=[]
    def marcar(numero, botao):
        if numero in selecionados:
            selecionados.remove(numero)
            botao.config(bg="#F0F0F0", fg="black")

        else:
            if len(selecionados) < limite:
                selecionados.append(numero)
                botao.config(bg=cor_marcado, fg="white")
    def fazer_aposta():
        if len(selecionados) == limite:
            carrinho.append({"jogo": titulo,"numeros": sorted(selecionados[:]),"preco":preco})
            print(carrinho)
            funcao_voltar()
    def limpar_aposta():
        selecionados.clear()

        for botao in botoes:
            botao.config(bg="#F0F0F0", fg="black")
    def fazer_surpresinha():
        for c in range(0,limite):
            selecionados.append(randint(0,total_numeros))
        carrinho.append({"jogo": titulo, "numeros": sorted(selecionados[:]), "preco": preco})
        print(carrinho)
        funcao_voltar()
    frame = tk.Frame(janela)

    area = tk.Frame(frame)
    area.pack(expand=True)

    texto = tk.Label(
        frame,
        text=f'{titulo:>20}',
        width=150,
        bg=cor_fundo,
        font=("Arial", 20, "bold"),
        anchor="nw"
    )
    texto.place(relx=0.0, rely=0.15)

    for i in range(1, total_numeros + 1):
        botao = tk.Button(
            area,
            text=f"{i:02}",
            width=5,
            height=2,
            font=("Arial", 14, "bold")
        )

        botao.config(command=lambda n=i, b=botao: marcar(n, b))

        linha = (i - 1) // colunas
        coluna = (i - 1) % colunas

        botao.grid(row=linha, column=coluna, padx=6, pady=6)
        botoes.append(botao)

    botao_cancelar = tk.Button(frame,text="Cancelar", font=("Arial", 30, "bold"),bg="red",fg='white',command=funcao_voltar)
    botao_cancelar.place(relx=0.01, rely=0.9)

    botao_confirmar = tk.Button(frame,text="Confirmar",font=("Arial", 30, "bold"),bg="green",fg='white',command=fazer_aposta)
    botao_confirmar.place(relx=0.87, rely=0.9)

    botao_surpresa= tk.Button(frame,text="Surpresa",font=("Arial",30,"bold"),command=fazer_surpresinha)
    botao_surpresa.place(relx=0.45, rely=0.9)
    frame.limpar_aposta = limpar_aposta



    return frame

