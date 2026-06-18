from src.banco.classe import *
import tkinter as tk

def abrir_tela_criar_conta(mostrar_tela,tela):
    mostrar_tela(tela)


def criar_conta(titular,senha,tipo,label,mostrar_tela):
    if titular and int(senha) and len(senha) == 4:
        if tipo=='Poupança':
            conta=(ContaPoupanca(titular=str(titular),senha=int(senha)))
            pass
        else:
            conta=(ContaCorrente(titular=str(titular),senha=int(senha)))
        banco.salvar_conta(conta)
        label.config(text=f'Titular: {conta.titular}\n'
f'Agencia: {conta.agencia}\n'
f'Conta: {conta.conta}\n'
f'Tipo: {conta.tipo}\n'
f'Senha: {conta.senha}\n',anchor="e")
        mostrar_tela()

def criar_tela_criar_conta(janela,mostrar_tela,tela_principal,tela_conta_criada
                           ,valida_texto,valida_num,label):
    def pegar_selecao():
        escolha = opcao.get()
        return escolha

    # TELA CRIAR CONTA
    tela = tk.Frame(janela)

    texto_agencia = tk.Label(tela, text='Agencia: 0732', font=('Arial', 25, 'bold'),
                             fg='black')
    texto_agencia.place(relx=0.01, rely=0.1)
    texto_titular = tk.Label(tela, text='Titular: ', font=('Arial', 25, 'bold'),
                             fg='black')
    texto_titular.place(relx=0.01, rely=0.2)

    titular = tk.Entry(tela, font=('Arial', 25, 'bold'), width=25, validate='key',
                       validatecommand=(valida_texto, "%P"))
    titular.place(relx=0.08, rely=0.2)
    texto_tipo = tk.Label(tela, text='Tipo:', font=('Arial', 25, 'bold'), )
    texto_tipo.place(relx=0.02, rely=0.3)
    opcao = tk.StringVar(value='Poupança')
    conta_poupança = tk.Radiobutton(tela, text='Poupança', font=('Arial', 25, 'bold'), variable=opcao,
                                    value='Poupança')
    conta_poupança.place(relx=0.08, rely=0.3)
    conta_corrente = tk.Radiobutton(tela, text='Corrente', font=('Arial', 25, 'bold'), variable=opcao,
                                    value='Corrente')
    conta_corrente.place(relx=0.2, rely=0.3)

    texto_criar_senha = tk.Label(tela, text='Senha: ', font=('Arial', 25, 'bold'), )
    texto_criar_senha.place(relx=0.01, rely=0.4)
    criar_senha = tk.Entry(tela, validate='key', validatecommand=(valida_num, "%P", 4), show='*',
                           font=('Arial', 30, 'bold'))
    criar_senha.place(relx=0.08, rely=0.4)

    botao_voltar = tk.Button(tela, text='Voltar', font=('Arial', 30, 'bold'),
                             bd=2, relief="solid", command=lambda:mostrar_tela(tela_principal))
    botao_voltar.place(relx=0.01, rely=0.9)


    botao_confirmar = tk.Button(tela, text='Confirmar', font=('Arial', 30, 'bold'),
                                bd=2, relief="solid", fg='white', bg='Green',
                                command=lambda: criar_conta(titular.get(), criar_senha.get(), pegar_selecao(),
                                                            label
                                                            , lambda: mostrar_tela(tela_conta_criada)))
    botao_confirmar.place(relx=0.87, rely=0.9)
    return tela
