import tkinter

def clicar_botao():
    texto.config(text='vc clicou no botao')

janela=tkinter.Tk()
janela.geometry('1920x1080')
janela.title('Sistema de Loterico Caixa')
janela.state('zoomed')

texto = tkinter.Label(janela, text='Clique no botao')
texto.pack(padx=10, pady=10)

botao_1= tkinter.Button(janela, text='Serviços Financeiros',font=('Arial',20,'bold'),
                        command=clicar_botao,bg='#69BCC7',fg='white')

botao_1.place(relx=0.01,rely=0.1)





janela.mainloop()