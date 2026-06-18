import tkinter as tk
from src.banco.classe import *



def criar_tela_saldo(janela,mostrar_tela,tela_principal,pegar_conta_atual,valida_num):
    def mostrar_saldo():
        conta = banco.buscar_conta(pegar_conta_atual())
        senha = senha_saldo.get()
        if not senha:
            print("Digite a senha")
            return
        if int(senha) == int(conta.senha):
            senha_saldo.delete(0, tk.END)
            cor = 'red' if conta.saldo < 0 else 'green'
            texto_titular.config(text=f'Titular: {conta.titular}\n'f'Conta: {conta.agencia}.{conta.conta}\n'
                                 , font=('Arial', 30, 'bold'), fg="black")
            texto_titular.place(relx=0.5, rely=0.25, anchor='center')
            texto_saldo_valor.config(text=f'Saldo: {conta.saldo:,.2f}', font=('Arial', 30, 'bold'), fg="white", bg=cor)
            texto_saldo_valor.place(relx=0.5, rely=0.35, anchor='center')
        else:
            print("Senha incorreta")

    def limpar_tela_saldo():
        senha_saldo.delete(0, tk.END)
        texto_titular.config(text='')
        texto_saldo_valor.config(text='', bg=tela.cget('bg'))

    tela = tk.Frame(janela)

    botao_voltar = tk.Button(tela, text='Voltar', font=('Arial', 30, 'bold'),
                             command=lambda:(mostrar_tela(tela_principal),limpar_tela_saldo()), bd=2, relief="solid")
    botao_voltar.place(relx=0.01, rely=0.9)

    texto_senha = tk.Label(tela, text='Digite sua senha', font=('Arial', 30, 'bold'))
    texto_senha.place(relx=0.5, rely=0.45, anchor='center')

    senha_saldo = tk.Entry(tela, font=('Arial', 30, 'bold'), show='*',validatecommand=(valida_num,'%P',4),validate='key')
    senha_saldo.place(relx=0.5, rely=0.55, anchor='center')

    botao_confirmar = tk.Button(tela, text='Confimar', font=('Arial', 30, 'bold'),
                                bg='green', fg='white', bd=2, relief="solid", command=mostrar_saldo)
    botao_confirmar.place(relx=0.87, rely=0.9)

    texto_titular = tk.Label(tela, font=('Arial', 30, 'bold'), fg="black")
    texto_titular.place(relx=0.5, rely=0.25, anchor='center')
    texto_saldo_valor = tk.Label(tela, font=('Arial', 30, 'bold'), fg="white")
    texto_saldo_valor.place(relx=0.5, rely=0.35, anchor='center')

    tela.limpar=limpar_tela_saldo

    return tela