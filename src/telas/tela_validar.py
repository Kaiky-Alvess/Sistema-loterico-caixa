import tkinter as tk
from src.banco.classe import *



def abrir_tela_validar(mostrar_tela,tela):
    mostrar_tela(tela)

def criar_tela_validar(janela,mostrar_tela,tela_principal,valida_num,abrir_tela_saque,
                       abrir_tela_deposito,abrir_tela_saldo,saque_ou_deposito,pegar_operacao):

    def validar_conta():
        if not agencia.get() or not numero_conta.get():
            print("Erro")
            return
        validar_agencia = int(agencia.get())
        validar_conta = int(numero_conta.get())
        contas = banco.listar_contas()
        operacao=pegar_operacao()
        for conta in contas:
            if validar_agencia == conta.agencia and validar_conta == conta.conta:
                conta_atual = conta.id
                if operacao == 'Saque':
                    abrir_tela_saque()
                elif operacao == 'Deposito':
                    abrir_tela_deposito()
                else:
                    abrir_tela_saldo()

    tela=tk.Frame(janela)
    texto = tk.Label(tela, text="Agência", font=('Arial', 30, 'bold'))
    texto.pack()
    agencia = tk.Entry(tela, validate='key', validatecommand=(valida_num, "%P", 4), font=('Arial', 30, 'bold'))
    agencia.pack()
    texto = tk.Label(tela, text="Conta", font=('Arial', 30, 'bold'))
    texto.pack()
    numero_conta = tk.Entry(tela, validate='key', validatecommand=(valida_num, "%P", 10),
                            font=('Arial', 30, 'bold'))
    numero_conta.pack()
    # BOTÃO CONFIRMAR
    botao_confirmar = tk.Button(tela, text='Confimar', font=('Arial', 30, 'bold'),
                                bg='green', fg='white', bd=2, relief="solid",
                                command=validar_conta)
    botao_confirmar.place(relx=0.87, rely=0.9)
    # BOTÃO CANCELAR
    botao_cancelar = tk.Button(tela, text='Cancelar', font=('Arial', 30, 'bold'),
                               bg='red', fg='white', command=lambda:mostrar_tela(tela_principal), bd=2, relief="solid")
    botao_cancelar.place(relx=0.01, rely=0.9)

    return tela