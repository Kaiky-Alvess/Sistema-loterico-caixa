from src.telas.tela_serviços import abrir_tela_serviços_financeiros, criar_tela_serviços_financeiros
from src.telas.tela_validar import *
from telas.tela_resultados import *
from loterias.loterias import criar_tela_loteria
from src.telas.tela_criar_conta import *
from banco.classe import *

banco.listar_contas()

carrinho=[]
conta_atual=0
indice_confirmacao=0
saque_ou_deposito= ''
jogos=['LOTOFACIL','MEGASENA', 'QUINA']
precos = {"Mega Sena": 6.00,"Lotofacil": 3.50,"Quina": 3.00}


def mostrar_tela(frame):
    global tela_atual
    if tela_atual is not None:
        tela_atual.pack_forget()
    frame.pack(fill='both', expand=True)
    tela_atual = frame

def tela_marcar_megasena():
    marcar_megaSena.limpar_aposta()
    mostrar_tela(marcar_megaSena)

def tela_marcar_lotofacil():
    marcar_lotofacil.limpar_aposta()
    mostrar_tela(marcar_lotofacil)

def tela_marcar_quina():
    marcar_quina.limpar_aposta()
    mostrar_tela(marcar_quina)



def abrir_tela_jogos():
    for widget in tela_jogos.winfo_children():
        if isinstance(widget, tk.Label):
            widget.destroy()
    pos=0
    for i,jogo in enumerate(carrinho):
        if jogo['nome']=='Lotofacil' or jogo['nome']=='Mega Sena' or jogo['nome']=='Quina':
            pos+=1
            mostrar_jogos = tk.Label(tela_jogos, text=f'{jogo['nome']} {pos}'
                                                      f'\n {jogo["numeros"]}',
                                     font=('Arial', 20, 'bold'))
            mostrar_jogos.pack()
    mostrar_tela(tela_jogos)

def pegar_operacao():
    return saque_ou_deposito

def tela_validar_saque():
    global saque_ou_deposito
    saque_ou_deposito = 'Saque'
    tela_validar.limpar()
    mostrar_tela(tela_validar)

def tela_validar_deposito():
    global saque_ou_deposito
    saque_ou_deposito = 'Deposito'
    tela_validar.limpar()
    mostrar_tela(tela_validar)

def tela_validar_saldo():
    global saque_ou_deposito
    saque_ou_deposito = 'Saldo'
    tela_validar.limpar()
    mostrar_tela(tela_validar)

def abrir_tela_saque():
    mostrar_tela(tela_saque)

def abrir_tela_deposito():
    mostrar_tela(tela_deposito)

def abrir_tela_saldo():
    mostrar_tela(tela_saldo)

def mostrar_saldo():
    conta = banco.buscar_conta(conta_atual)
    senha = senha_saldo.get()
    if not senha:
        print("Digite a senha")
        return
    if int(senha) == int(conta.senha):
        senha_saldo.delete(0, tk.END)
        cor = 'red' if conta.saldo < 0 else 'green'
        texto_titular.config(text=f'Titular: {conta.titular}\n'f'Conta: {conta.agencia}.{conta.conta}\n'
                         , font=('Arial',30,'bold'), fg="black")
        texto_titular.place(relx=0.5,rely=0.25,anchor='center')
        texto_saldo_valor.config(text=f'Saldo: {conta.saldo:,.2f}',font=('Arial',30,'bold'),fg="white",bg=cor)
        texto_saldo_valor.place(relx=0.5,rely=0.35,anchor='center')
    else:
        print("Senha incorreta")

def sacar():
    conta = banco.buscar_conta(conta_atual)
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
        carrinho.append({"nome": "Saque","numeros": None,"preco": float(valor * -1)})
        mostrar_tela(tela_principal)
        print(conta.saldo)
    else:
        print("Senha incorreta")

def adicionar_deposito():
    conta = banco.buscar_conta(conta_atual)
    valor=int(valor_deposito.get())
    if valor > 5000:
        return mostrar_tela(tela_principal)
    carrinho.append({"nome": 'Deposito', "conta": conta.conta, "preco": float(valor), "agencia": conta.agencia
                     ,"ID": conta.id})
    mostrar_tela(tela_principal)
    return valor


def confirmar_deposito():
    global indice_confirmacao
    item = carrinho[indice_confirmacao]
    conta = banco.buscar_conta(item["ID"])
    conta.depositar(item["preco"])
    banco.atualizar_conta(conta)
    indice_confirmacao += 1
    abrir_tela_confirmar()
    print(conta.saldo)

def mostrar_conta(item):
    for widget in tela_confirmar.winfo_children():
        if isinstance(widget, tk.Label):
            widget.destroy()
    conta = banco.buscar_conta(item["ID"])
    titular = tk.Label(tela_confirmar,text=f'{conta.titular}',font=('Arial', 30),width=30)
    titular.place(relx=0.5, rely=0.25, anchor='center')
    valor = tk.Label(tela_confirmar,text=f'R${item["preco"]:,.2f}',font=('Arial', 30))
    valor.place(relx=0.5, rely=0.35, anchor='center')

def calcular_carrinho():
    total = sum(item["preco"] for item in carrinho)
    label_total.config(text=f"Total: R$ {total:.2f}")

def finalizar_atendimento():
    carrinho.clear()
    atualizar_carrinho()
    calcular_carrinho()
    mostrar_tela(tela_principal)

def abrir_tela_principal():
    #limpar_campos()
    mostrar_tela(tela_principal)

def atualizar_carrinho():
    for widget in frame_lista.winfo_children():
        widget.destroy()
    for i, item in enumerate(carrinho):
        linha = tk.Frame(frame_lista)
        linha.pack(fill="x", pady=5, padx=10)
        if item["preco"]<0:
            texto = tk.Label(linha, text=f'{item["nome"]} |  R${item["preco"] * -1:.2f}', font=("Arial", 16),anchor="w")
            texto.pack(side="left")
        else:
            texto = tk.Label(linha,text=f'{item["nome"]} |  R${item["preco"]:.2f}',font=("Arial", 16),anchor="w")
            texto.pack(side="left")
        if not item["nome"] == "Saque":
            botao_remover = tk.Button(linha,text="—",font=("Arial", 14, "bold")
                                      ,bg="red",fg="white",command=lambda idx=i: remover_aposta(idx))
            botao_remover.pack(side="left")

        calcular_carrinho()

def remover_aposta(indice):
    carrinho.pop(indice)
    atualizar_carrinho()
    calcular_carrinho()

def abrir_tela_atendimento():
    atualizar_carrinho()
    calcular_carrinho()
    mostrar_tela(tela_atendimento)

def abrir_tela_confirmar():
    global indice_confirmacao
    if indice_confirmacao >= len(carrinho):
        finalizar_atendimento()
        indice_confirmacao = 0
        return
    item = carrinho[indice_confirmacao]
    if item["nome"] == "Deposito":
        mostrar_conta(item)
        mostrar_tela(tela_confirmar)
    else:
        indice_confirmacao += 1
        abrir_tela_confirmar()

def cancelar_operação():
    #limpar_campos()
    mostrar_tela(tela_principal)

def validar_num(texto,total_algarismos):
    return texto == "" or (texto.isdigit() and len(texto) <= int(total_algarismos))

def validar_txt(texto_inserido):
    return not any(char.isdigit() for char in texto_inserido)


def limpar_campos():
    global conta_atual
    conta_atual = 0
    valor_saque.delete(0, tk.END)
    senha_saque.delete(0, tk.END)
    valor_deposito.delete(0, tk.END)
    senha_saldo.delete(0, tk.END)
    #titular.delete(0, tk.END)
    texto_titular.config(text='')
    texto_saldo_valor.config(text='', bg=tela_saldo.cget('bg'))
    #criar_senha.delete(0, tk.END)

def abrir_tela_conta():
    mostrar_tela(tela_criar_conta)
def definir_conta_atual(id_conta):
    global conta_atual
    conta_atual = id_conta




#JANELA
janela=tk.Tk()
janela.geometry('1920x1080')
janela.title('Sistema de Loterico Caixa')
janela.state('zoomed')
logo = tk.PhotoImage(file='../assets/imagens/logo_caixa.png')
janela.iconphoto(True,logo)


valida_num = janela.register(validar_num)
valida_texto = janela.register(validar_txt)

#TELA PRINCIPAL
tela_principal=tk.Frame(janela)
tela_principal.pack(fill='both', expand=True)
tela_atual = tela_principal

    #BOTÃO SERVIÇOS
botao_serviços= tk.Button(tela_principal, text='Serviços Financeiros', font=('Arial', 25, 'bold'),
                          command=lambda:abrir_tela_serviços_financeiros(mostrar_tela,tela_servicos), bg='#69BCC7', fg='white'
                          ,bd=2, relief='solid',width=20)
botao_serviços.place(relx=0.01, rely=0.2)
    #BOTÃO RESULTADOS
botao_resultados=tk.Button(tela_principal, text='Ultimos Resultados',
                           font=('Arial', 25, 'bold'), bg='#69BCC7', fg='white'
                           ,bd=2, relief='solid',width=20,
                           command=lambda:abrir_tela_resultados(mostrar_tela,tela_resultados))
botao_resultados.place(relx=0.25, rely=0.2)

    #BOTÃO ATENDIMENTO
botao_atendimento=tk.Button(tela_principal, text='Atendimento',font=('Arial', 25, 'bold'),
                            bg='#69BCC7', fg='white'
                           ,bd=2, relief='solid',width=20,command=abrir_tela_atendimento)
botao_atendimento.place(relx=0.01, rely=0.4)

    #BOTÃO CRIAR CONTA
botao_criar_conta=tk.Button(tela_principal,text='Criar Conta',font=('Arial', 25, 'bold'),
                            bg='#69BCC7', fg='white'
                            ,bd=2,relief="solid",width=20,command=abrir_tela_conta)
botao_criar_conta.place(relx=0.25, rely=0.4)

    #BOTÃO MEGA SENA
botao_megaSena=tk.Button(tela_principal, text='MEGA SENA', font=('Arial', 30, 'bold'),
                                   bg='green', fg='white', bd=True, relief="solid"
                                   ,width=20,command=tela_marcar_megasena)
botao_megaSena.place(relx=0.7, rely=0.2)

marcar_megaSena = criar_tela_loteria(janela, abrir_tela_principal,"Mega Sena",60,6,10,
                                     "green","#DAA520",carrinho,precos["Mega Sena"])

    #BOTÃO LOTOFAICL
botao_lotofacil=tk.Button(tela_principal, text='LOTOFACIL', font=('Arial', 30, 'bold'),
                                    bg='purple', fg='white', bd=True, relief="solid"
                                    ,width=20,command=tela_marcar_lotofacil)
botao_lotofacil.place(relx=0.7, rely=0.3)
marcar_lotofacil = criar_tela_loteria(janela,abrir_tela_principal,"Lotofacil",25,15,5,
                                      "purple","#DAA520",carrinho,precos["Lotofacil"])

    #BOTÃO QUINA
botao_quina=tk.Button(tela_principal, text='QUINA', font=('Arial', 30, 'bold'),
                                bg='blue', fg='white', bd=True, relief="solid",
                                width=20,command=tela_marcar_quina)
botao_quina.place(relx=0.7, rely=0.4)

marcar_quina= criar_tela_loteria(janela,abrir_tela_principal,"Quina",80,5,10,
                                 "blue","#DAA520",carrinho,precos["Quina"])



#TELA CONTA CRIADA
tela_conta_criada=tk.Frame(janela)

informacoes = tk.Label(tela_conta_criada, font=('Arial', 25, 'bold'), )
informacoes.place(relx=0.01, rely=0.1)

botao_voltar=tk.Button(tela_conta_criada,text='Voltar',font=('Arial', 30, 'bold'),
                       command=abrir_tela_principal)
botao_voltar.place(relx=0.01, rely=0.9)

tela_criar_conta= criar_tela_criar_conta(janela,mostrar_tela,tela_principal,tela_conta_criada,
                                         valida_texto,valida_num,informacoes)



#TELA DE VALIDAÇÃO
tela_validar= criar_tela_validar(janela, mostrar_tela, tela_principal, valida_num, abrir_tela_saque, abrir_tela_deposito,
                                 abrir_tela_saldo, saque_ou_deposito,pegar_operacao,definir_conta_atual)



#TELA SERVIÇOS FINANCEIROS
tela_servicos=criar_tela_serviços_financeiros(janela,mostrar_tela,tela_principal,tela_validar_saque,
                                              tela_validar_deposito,tela_validar_saldo)

#TELA DE RESULTADOS
tela_resultados=criar_tela_resultados(janela,mostrar_tela,tela_principal)


#TELA DE ATENDIMENTO

tela_atendimento=tk.Frame(janela)

texto = tk.Label(tela_atendimento, font=("Arial", 16))
texto.pack()
label_total = tk.Label(tela_atendimento, font=("Arial", 18, "bold"))
label_total.pack()

frame_lista = tk.Frame(tela_atendimento)
frame_lista.pack(pady=20, fill="both", expand=True)

botao_ver_jogos= tk.Button(tela_atendimento,text='Ver Jogos', font=('Arial', 30, 'bold'),
                           bd=2, relief="solid",command=abrir_tela_jogos)
botao_ver_jogos.place(relx=0.5, rely=0.9, anchor='center')

botao_finalizar= tk.Button(tela_atendimento, text= 'Finalizar',font=('Arial', 30, 'bold'),
                           command=abrir_tela_confirmar,bd=2, relief="solid")
botao_finalizar.place(relx=0.89, rely=0.9)

botao_voltar=tk.Button(tela_atendimento, text='Voltar', font=('Arial', 30, 'bold'),
                       command=abrir_tela_principal,bd=2, relief="solid")
botao_voltar.place(relx=0.01, rely=0.9)

#TELA DE SAQUE
tela_saque=tk.Frame(janela)

tela_deposito=tk.Frame(janela)



    #BOTÃO CANCELAR
botao_cancelar=tk.Button(tela_saque, text='Cancelar', font=('Arial', 30, 'bold'),
                         bg='red',fg='white',command=cancelar_operação,bd=2, relief="solid")
botao_cancelar.place(relx=0.01, rely=0.9)

    #BOTÃO CONFIRMAR
botao_confirmar=tk.Button(tela_saque,text='Confimar', font=('Arial', 30, 'bold'),
                          bg='green',fg='white',bd=2, relief="solid",command=sacar)
botao_confirmar.place(relx=0.87, rely=0.9)

texto_valor=tk.Label(tela_saque, text='Digite o valor \nMin: 5,00 | Max: 5.000,00', font=('Arial', 30, 'bold'))
texto_valor.place(relx=0.5,rely=0.25,anchor='center')
valor_saque=tk.Entry(tela_saque,font=('Arial', 30, 'bold'))
valor_saque.place(relx=0.5,rely=0.35,anchor='center')
texto_senha=tk.Label(tela_saque,text='Digite sua senha', font=('Arial', 30, 'bold'))
texto_senha.place(relx=0.5,rely=0.45,anchor='center')
senha_saque=tk.Entry(tela_saque,font=('Arial', 30, 'bold'),show='*')
senha_saque.place(relx=0.5,rely=0.55,anchor='center')

#TELA DEPOSITO

    #BOTÃO CANCELAR
botao_cancelar=tk.Button(tela_deposito, text='Cancelar', font=('Arial', 30, 'bold'),
                         bg='red',fg='white',command=cancelar_operação,bd=2, relief="solid")
botao_cancelar.place(relx=0.01, rely=0.9)

    #BOTÃO CONFIRMAR
botao_confirmar=tk.Button(tela_deposito,text='Confimar', font=('Arial', 30, 'bold'),
                          bg='green',fg='white',bd=2, relief="solid",command=adicionar_deposito)
botao_confirmar.place(relx=0.87, rely=0.9)



texto_valor=tk.Label(tela_deposito, text='Digite o valor \nMin: 5,00 | Max: 5.000,00', font=('Arial',30, 'bold'))
texto_valor.place(relx=0.5,rely=0.25,anchor='center')
valor_deposito=tk.Entry(tela_deposito,font=('Arial', 30, 'bold'))
valor_deposito.place(relx=0.5,rely=0.35,anchor='center')

#TELA CONFIRMAR DEPOSITO
tela_confirmar=tk.Frame(janela)



    #BOTÃO CANCELAR
botao_cancelar=tk.Button(tela_confirmar, text='Cancelar', font=('Arial', 30, 'bold'),
                         bg='red',fg='white',command=cancelar_operação,bd=2, relief="solid")
botao_cancelar.place(relx=0.01, rely=0.9)

    #BOTÃO CONFIMAR
botao_confirmar=tk.Button(tela_confirmar, text='Confimar', font=('Arial', 30, 'bold'),
                          bg='green',fg='white',command=confirmar_deposito,bd=2, relief="solid")
botao_confirmar.place(relx=0.87, rely=0.9)

#TELA SALDO
tela_saldo=tk.Frame(janela)

botao_voltar=tk.Button(tela_saldo, text='Voltar', font=('Arial', 30, 'bold'),
                       command=abrir_tela_principal,bd=2, relief="solid")
botao_voltar.place(relx=0.01, rely=0.9)

texto_senha=tk.Label(tela_saldo,text='Digite sua senha', font=('Arial', 30, 'bold'))
texto_senha.place(relx=0.5,rely=0.45,anchor='center')

senha_saldo=tk.Entry(tela_saldo,font=('Arial', 30, 'bold'),show='*')
senha_saldo.place(relx=0.5,rely=0.55,anchor='center')

botao_confirmar=tk.Button(tela_saldo,text='Confimar', font=('Arial', 30, 'bold'),
                          bg='green',fg='white',bd=2, relief="solid",command=mostrar_saldo)
botao_confirmar.place(relx=0.87, rely=0.9)

texto_titular = tk.Label(tela_saldo,font=('Arial',30,'bold'),fg="black")
texto_titular.place(relx=0.5,rely=0.25,anchor='center')
texto_saldo_valor = tk.Label(tela_saldo,font=('Arial',30,'bold'), fg="white")
texto_saldo_valor.place(relx=0.5,rely=0.35,anchor='center')


tela_jogos=tk.Frame(janela)



botao_voltar=tk.Button(tela_jogos,text='Voltar', font=('Arial', 30, 'bold'),command=abrir_tela_atendimento,
                       bd=2, relief="solid")
botao_voltar.place(relx=0.01, rely=0.9)

janela.mainloop()