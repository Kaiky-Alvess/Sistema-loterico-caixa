import tkinter as tk


def abrir_tela_serviços_financeiros(mostrar_tela,tela):
    mostrar_tela(tela)

def criar_tela_serviços_financeiros(janela,mostrar_tela):
    tela = tk.Frame(janela)

    botao_saque = tk.Button(tela, text=f'Saque', font=('Arial', 30, 'bold'),
                            command=lambda:mostrar_tela("validar"), bg='#69BCC7', fg='white', bd=True, relief="solid", width=10)
    botao_saque.place(relx=0.01, rely=0.25)

    botao_deposito = tk.Button(tela, text=f'Depósito', font=('Arial', 30, 'bold'),
                               bg='#69BCC7', fg='white', bd=True, relief="solid",
                               command=lambda:mostrar_tela("validar"),
                               width=10)
    botao_deposito.place(relx=0.2, rely=0.25)

    botao_voltar = tk.Button(tela, text='Voltar', font=('Arial', 30, 'bold'),
                             command=lambda:mostrar_tela("principal"), bd=2, relief="solid")
    botao_voltar.place(relx=0.01, rely=0.9)

    botao_saldo = tk.Button(tela, text=f'Saldo', font=('Arial', 30, 'bold'),
                            bg='#69BCC7', fg='white', bd=True, relief="solid", width=10,
                            command=lambda:mostrar_tela("validar"))
    botao_saldo.place(relx=0.01, rely=0.35)

    return tela