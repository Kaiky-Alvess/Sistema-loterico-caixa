import tkinter as tk
from src.banco.classe import *

def abrir_tela_saque(mostrar_tela,tela):
    mostrar_tela(tela)

def criar_tela_saque(janela,mostrar_tela,tela_principal,valida_num,carrinho,pegar_conta_atual):
    def sacar():
        conta=banco.buscar_conta(pegar_conta_atual())
        valor_texto = valor_saque.get()
        senha_texto = senha_saque.get()
        if not valor_texto or not senha_texto:
            print("Preencha todos os campos")
            return
        valor = int(valor_texto)
        if valor < 5:
            print("Valor mínimo é 5")
            return
        if valor > 5000 or valor > conta.saldo:
            print("Valor inválido")
            return mostrar_tela(tela_principal)
        if int(senha_texto) == int(conta.senha):
            conta.sacar(valor)
            banco.atualizar_conta(conta)
            carrinho.append({"nome": "Saque", "numeros": None, "preco": float(valor * -1)})
            mostrar_tela(tela_principal)
            print(conta.saldo)
        else:
            print("Senha incorreta")
    def limpar_tela_saque():
        valor_saque.delete(0, tk.END)
        senha_saque.delete(0, tk.END)

    tela=tk.Frame(janela)

    texto_valor = tk.Label(tela, text='Digite o valor \nMin: 5,00 | Max: 5.000,00', font=('Arial', 30, 'bold'))
    texto_valor.place(relx=0.5, rely=0.25, anchor='center')
    valor_saque = tk.Entry(tela, font=('Arial', 30, 'bold'))
    valor_saque.place(relx=0.5, rely=0.35, anchor='center')
    texto_senha = tk.Label(tela, text='Digite sua senha', font=('Arial', 30, 'bold'))
    texto_senha.place(relx=0.5, rely=0.45, anchor='center')
    senha_saque = tk.Entry(tela,validate='key',validatecommand=(valida_num,"%P",4),
                           font=('Arial', 30, 'bold'), show='*')
    senha_saque.place(relx=0.5, rely=0.55, anchor='center')

    botao_cancelar = tk.Button(tela, text='Cancelar', font=('Arial', 30, 'bold'),
                               bg='red', fg='white', command=lambda:mostrar_tela(tela_principal) , bd=2, relief="solid")
    botao_cancelar.place(relx=0.01, rely=0.9)

    botao_confirmar = tk.Button(tela, text='Confimar', font=('Arial', 30, 'bold'),
                                bg='green', fg='white', bd=2, relief="solid", command=sacar)
    botao_confirmar.place(relx=0.87, rely=0.9)

    tela.limpar= limpar_tela_saque
    return tela

