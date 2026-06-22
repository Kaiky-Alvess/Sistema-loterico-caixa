import tkinter as tk

def criar_tela_principal(janela, mostrar_tela):
    tela = tk.Frame(janela)
    botao_servicos = tk.Button(tela, text='Serviços Financeiros', font=('Arial', 25, 'bold'),
                               command=lambda: mostrar_tela("servicos_financeiros"),
                               bg='#69BCC7', fg='white'
                               , bd=2, relief='solid', width=20)
    botao_servicos.place(relx=0.01, rely=0.2)

    botao_resultados = tk.Button(tela, text='Ultimos Resultados',
                                 font=('Arial', 25, 'bold'), bg='#69BCC7', fg='white'
                                 , bd=2, relief='solid', width=20,
                                 command=lambda: mostrar_tela("resultados"))
    botao_resultados.place(relx=0.25, rely=0.2)

    botao_atendimento = tk.Button(tela, text='Atendimento', font=('Arial', 25, 'bold'),
                                  bg='#69BCC7', fg='white'
                                  , bd=2, relief='solid', width=20, command=lambda:mostrar_tela("atendimento"))
    botao_atendimento.place(relx=0.01, rely=0.4)

    botao_criar_conta = tk.Button(tela, text='Criar Conta', font=('Arial', 25, 'bold'),
                                  bg='#69BCC7', fg='white'
                                  , bd=2, relief="solid", width=20,
                                  command=lambda:mostrar_tela("criar_conta"))
    botao_criar_conta.place(relx=0.25, rely=0.4)

    # BOTÃO MEGA SENA
    botao_megaSena = tk.Button(tela, text='MEGA SENA', font=('Arial', 30, 'bold'),
                               bg='green', fg='white', bd=True, relief="solid"
                               , width=20, command=lambda:mostrar_tela("mega_sena"))
    botao_megaSena.place(relx=0.7, rely=0.2)

    # BOTÃO LOTOFAICL
    botao_lotofacil = tk.Button(tela, text='LOTOFACIL', font=('Arial', 30, 'bold'),
                                bg='purple', fg='white', bd=True, relief="solid"
                                , width=20, command=lambda:mostrar_tela("lotofacil"))
    botao_lotofacil.place(relx=0.7, rely=0.3)

    # BOTÃO QUINA
    botao_quina = tk.Button(tela, text='QUINA', font=('Arial', 30, 'bold'),
                            bg='blue', fg='white', bd=True, relief="solid",
                            width=20, command=lambda:mostrar_tela("quina"))
    botao_quina.place(relx=0.7, rely=0.4)

    return tela