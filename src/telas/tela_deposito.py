import tkinter as tk
from src.banco.classe import *



def criar_tela_deposito(janela,mostrar_tela,carrinho,pegar_conta_atual):
    def adicionar_deposito():
        conta = banco.buscar_conta(pegar_conta_atual())
        valor = int(valor_deposito.get())
        if valor > 5000:
            return mostrar_tela("principal")
        carrinho.append({"nome": 'Deposito', "conta": conta.conta, "preco": float(valor), "agencia": conta.agencia
                            , "ID": conta.id})
        mostrar_tela("principal")
        return valor

    def limpar_tela_deposito():
        valor_deposito.delete(0, tk.END)

    tela=tk.Frame(janela)

    # BOTÃO CANCELAR
    botao_cancelar = tk.Button(tela, text='Cancelar', font=('Arial', 30, 'bold'),
                               bg='red', fg='white', command=lambda:mostrar_tela("principal"), bd=2, relief="solid")
    botao_cancelar.place(relx=0.01, rely=0.9)

    # BOTÃO CONFIRMAR
    botao_confirmar = tk.Button(tela, text='Confimar', font=('Arial', 30, 'bold'),
                                bg='green', fg='white', bd=2, relief="solid", command=adicionar_deposito)
    botao_confirmar.place(relx=0.87, rely=0.9)

    texto_valor = tk.Label(tela, text='Digite o valor \nMin: 5,00 | Max: 5.000,00', font=('Arial', 30, 'bold'))
    texto_valor.place(relx=0.5, rely=0.25, anchor='center')
    valor_deposito = tk.Entry(tela, font=('Arial', 30, 'bold'))
    valor_deposito.place(relx=0.5, rely=0.35, anchor='center')

    tela.limpar=limpar_tela_deposito

    return tela