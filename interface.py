import tkinter as tk

def tela_serviçosFinanceiros():
    tela_principal.pack_forget()
    tela_serviços.pack(fill='both', expand=True)
def abrir_tela_saque():
    tela_serviços.pack_forget()
    tela_saque.pack(fill='both', expand=True)
def abrir_tela_principal():
    tela_serviços.pack_forget()
    tela_principal.pack(fill='both', expand=True)
def cancelar_operação():
    tela_saque.pack_forget()
    tela_principal.pack(fill='both', expand=True)

#JANELA
janela=tk.Tk()
janela.geometry('1920x1080')
janela.title('Sistema de Loterico Caixa')
janela.state('zoomed')

#TELA PRINCIPAL
tela_principal=tk.Frame(janela)
tela_principal.pack(fill='both', expand=True)

    #BOTÃO SERVIÇOS
botao_serviços= tk.Button(tela_principal, text='Serviços Financeiros', font=('Arial', 30, 'bold'),
                          command=tela_serviçosFinanceiros, bg='#69BCC7', fg='white')
botao_serviços.place(relx=0.01, rely=0.1)

#TELA DE SERVIÇOS
tela_serviços=tk.Frame(janela)


    #BOTÃO SAQUE
botao_saque= tk.Button(tela_serviços, text=f'{"Saque":^15}', font=('Arial', 30, 'bold'),
                       command=abrir_tela_saque, bg='#69BCC7', fg='white', bd=True, relief="solid")
botao_saque.place(relx=0.01, rely=0.25)

    #BOTÃO DEPÓSITO
botao_deposito= tk.Button(tela_serviços, text=f'{"Depósito":^15}', font=('Arial', 30, 'bold'),
                           bg='#69BCC7', fg='white',bd=True,relief="solid")
botao_deposito.place(relx=0.2, rely=0.25)

    #BOTÃO VOLTAR
botao_voltar=tk.Button(tela_serviços, text='Voltar', font=('Arial', 30, 'bold'),
                       command=abrir_tela_principal,bd=2, relief="solid")
botao_voltar.place(relx=0.01, rely=0.9)

#TELA DE SAQUE
tela_saque=tk.Frame(janela)

    #BOTÃO CANCELAR
botao_cancelar=tk.Button(tela_saque, text='Cancelar', font=('Arial', 30, 'bold'),
                         fg='red',command=cancelar_operação,bd=2, relief="solid")
botao_cancelar.place(relx=0.01, rely=0.9)

    #BOTÃO CONFIRMAR
botao_confirmar=tk.Button(tela_saque,text='Confimar', font=('Arial', 30, 'bold'),
                          fg='green',bd=2, relief="solid")
botao_confirmar.place(relx=0.87, rely=0.9)

texto_valor=tk.Label(tela_saque, text='Digite o valor \nMin: 5,00 | Max: 5.000,00', font=('Arial', 10, 'bold'))
texto_valor.place(relx=0.45,rely=0.45)
valor_saque=tk.Entry(tela_saque)
valor_saque.place(relx=0.45,rely=0.5)

janela.mainloop()