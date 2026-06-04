import tkinter as tk


def abrir_tela_serviços_financeiros(mostrar_tela,tela):
    mostrar_tela(tela)

def criar_tela_serviços_financeiros(janela,mostrar_tela,tela_principal,tela_validar_saque,tela_validar_deposito,
                                    tela_validar_saldo):
    tela_serviços = tk.Frame(janela)
    # BOTÃO SAQUE
    botao_saque = tk.Button(tela_serviços, text=f'Saque', font=('Arial', 30, 'bold'),
                            command=tela_validar_saque, bg='#69BCC7', fg='white', bd=True, relief="solid", width=10)
    botao_saque.place(relx=0.01, rely=0.25)

    # BOTÃO DEPÓSITO
    botao_deposito = tk.Button(tela_serviços, text=f'Depósito', font=('Arial', 30, 'bold'),
                               bg='#69BCC7', fg='white', bd=True, relief="solid", command=tela_validar_deposito,
                               width=10)
    botao_deposito.place(relx=0.2, rely=0.25)

    # BOTÃO VOLTAR (tela serviços)
    botao_voltar = tk.Button(tela_serviços, text='Voltar', font=('Arial', 30, 'bold'),
                             command=lambda:mostrar_tela(tela_principal), bd=2, relief="solid")
    botao_voltar.place(relx=0.01, rely=0.9)

    # BOTÃO SALDO
    botao_saldo = tk.Button(tela_serviços, text=f'Saldo', font=('Arial', 30, 'bold'),
                            bg='#69BCC7', fg='white', bd=True, relief="solid", width=10, command=tela_validar_saldo)
    botao_saldo.place(relx=0.01, rely=0.35)
    return tela_serviços