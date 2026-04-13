import tkinter as tk

def tela_serviçosFinanceiros():
    tela_principal.pack_forget()
    tela_serviços.pack(fill='both', expand=True)


def funcao_saque():
    texto.config(text='vc clicou no botao')
def funcao_tela_saque():
    tela_serviços.pack_forget()
    tela_saque.pack(fill='both', expand=True)
janela=tk.Tk()
janela.geometry('1920x1080')
janela.title('Sistema de Loterico Caixa')
janela.state('zoomed')

tela_principal=tk.Frame(janela)
tela_principal.pack(fill='both', expand=True)

texto = tk.Label(tela_principal, text='Clique no botao')
texto.pack(padx=10, pady=10)

botao_serviços= tk.Button(tela_principal, text='Serviços Financeiros', font=('Arial', 30, 'bold'),
                          command=tela_serviçosFinanceiros, bg='#69BCC7', fg='white')
botao_serviços.place(relx=0.01, rely=0.1)


tela_serviços=tk.Frame(janela)

texto = tk.Label(tela_serviços, text='Você está na Tela 2')
texto.pack(pady=50)
texto2 = tk.Label(tela_serviços, text='Clique no botao')

botao_saque= tk.Button(tela_serviços, text=f'{"Saque":^15}', font=('Arial', 30, 'bold'),
                          command=funcao_tela_saque, bg='#69BCC7', fg='white',bd=True,relief="solid")
botao_saque.place(relx=0.01, rely=0.25)
botao_deposito= tk.Button(tela_serviços, text=f'{"Depósito":^15}', font=('Arial', 30, 'bold'),
                          command=funcao_saque, bg='#69BCC7', fg='white',bd=True,relief="solid")
botao_deposito.place(relx=0.2, rely=0.25)

tela_saque=tk.Frame(janela)
valor_saque=tk.Entry(tela_saque)
valor_saque.place(relx=0.5,rely=0.5)

janela.mainloop()