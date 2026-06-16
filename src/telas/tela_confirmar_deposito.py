import tkinter as tk
from src.banco.classe import *

indice_confirmacao=0


def criar_tela_confirmar_deposito(janela,mostrar_tela,tela_principal,carrinho,finalizar_atendimento):
    def mostrar_conta(item):
        for widget in tela.winfo_children():
            if isinstance(widget, tk.Label):
                widget.destroy()
        conta = banco.buscar_conta(item["ID"])
        titular = tk.Label(tela, text=f'{conta.titular}', font=('Arial', 30), width=30)
        titular.place(relx=0.5, rely=0.25, anchor='center')
        valor = tk.Label(tela, text=f'R${item["preco"]:,.2f}', font=('Arial', 30))
        valor.place(relx=0.5, rely=0.35, anchor='center')

    def abrir_tela_confirmar():
        global indice_confirmacao
        if indice_confirmacao >= len(carrinho):
            finalizar_atendimento()
            indice_confirmacao = 0
            return
        item = carrinho[indice_confirmacao]
        if item["nome"] == "Deposito":
            mostrar_conta(item)
            mostrar_tela(tela)
        else:
            indice_confirmacao += 1
            abrir_tela_confirmar()

    def confirmar_deposito():
        global indice_confirmacao
        item = carrinho[indice_confirmacao]
        conta = banco.buscar_conta(item["ID"])
        conta.depositar(item["preco"])
        banco.atualizar_conta(conta)
        indice_confirmacao += 1
        abrir_tela_confirmar()
        print(conta.saldo)

    tela = tk.Frame(janela)

    botao_cancelar = tk.Button(tela, text='Cancelar', font=('Arial', 30, 'bold'),
                               bg='red', fg='white', command=lambda:mostrar_tela(tela_principal), bd=2, relief="solid")
    botao_cancelar.place(relx=0.01, rely=0.9)

    botao_confirmar = tk.Button(tela, text='Confimar', font=('Arial', 30, 'bold'),
                                bg='green', fg='white', command=confirmar_deposito, bd=2, relief="solid")
    botao_confirmar.place(relx=0.87, rely=0.9)

    return tela,abrir_tela_confirmar