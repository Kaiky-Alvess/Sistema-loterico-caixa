import tkinter as tk

def mostrar_tela(frame):
    global tela_atual

    if tela_atual is not None:
        tela_atual.pack_forget()

    frame.pack(fill='both', expand=True)
    tela_atual = frame

def tela_serviçosFinanceiros():
    mostrar_tela(tela_serviços)

def abrir_tela_resultados():
    mostrar_tela(tela_resultados)

def abrir_tela_saque():
    mostrar_tela(tela_saque)

def abrir_tela_principal():
    mostrar_tela(tela_principal)

def cancelar_operação():
    mostrar_tela(tela_principal)

#JANELA
janela=tk.Tk()
janela.geometry('1920x1080')
janela.title('Sistema de Loterico Caixa')
janela.state('zoomed')

#TELA PRINCIPAL
tela_principal=tk.Frame(janela)
tela_principal.pack(fill='both', expand=True)
tela_atual = tela_principal

    #BOTÃO SERVIÇOS
botao_serviços= tk.Button(tela_principal, text='Serviços Financeiros', font=('Arial', 25, 'bold'),
                          command=tela_serviçosFinanceiros, bg='#69BCC7', fg='white'
                          ,bd=2, relief='solid',width=20)
botao_serviços.place(relx=0.01, rely=0.2)
    #BOTÃO RESULTADOS
botao_resultados=tk.Button(tela_principal, text='Ultimos Resultados',
                           font=('Arial', 25, 'bold'), bg='#69BCC7', fg='white'
                           ,bd=2, relief='solid',width=20,command=abrir_tela_resultados)
botao_resultados.place(relx=0.25, rely=0.2)



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

    #BOTÃO VOLTAR (tela serviços)
botao_voltar=tk.Button(tela_serviços, text='Voltar', font=('Arial', 30, 'bold'),
                       command=abrir_tela_principal,bd=2, relief="solid")
botao_voltar.place(relx=0.01, rely=0.9)

#TELA DE RESULTADOS
tela_resultados=tk.Frame(janela)

    #BOTÃO RESULTADO DA MEGA SENA
botao_resultado_megaSena=tk.Button(tela_resultados, text='MEGA SENA', font=('Arial', 30, 'bold'),
                                   bg='green', fg='white', bd=True, relief="solid"
                                   ,width=10)
botao_resultado_megaSena.place(relx=0.2, rely=0.2)
    #BOTÃO RESULTADO DA LOTOFACIL
botao_resultado_lotofacil=tk.Button(tela_resultados, text='LOTOFACIL', font=('Arial', 30, 'bold'),
                                    bg='purple', fg='white', bd=True, relief="solid"
                                    ,width=10)
botao_resultado_lotofacil.place(relx=0.4, rely=0.2)
    #BOTÃO RESULTADO DA QUINA
botao_resultado_quina=tk.Button(tela_resultados, text='QUINA', font=('Arial', 30, 'bold'),
                                bg='#A02B93', fg='white', bd=True, relief="solid",
                                width=10)
botao_resultado_quina.place(relx=0.6, rely=0.2)


    #BOTÃO VOLTAR (tela resultados)
botao_voltar=tk.Button(tela_resultados, text='Voltar', font=('Arial', 30, 'bold'),
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