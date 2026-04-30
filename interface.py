import tkinter as tk
import requests

from loterias.loterias import criar_tela_loteria

import sqlite3

carrinho=[]

precos = {"Mega Sena": 6.00,"Lotofacil": 3.50,"Quina": 3.00}
kaiky={"agencia":1234,"conta":56789}


def buscar_lotofacil():
    url = "https://loteriascaixa-api.herokuapp.com/api/lotofacil/latest"
    resposta = requests.get(url)
    dados = resposta.json()
    numeros = dados["dezenas"]
    concurso = dados["concurso"]
    texto_resultado.config(text=f"Lotofácil\nConcurso {concurso}\n" + " - ".join(numeros),
                           bg="purple", fg="white")

def buscar_megasena():
    url = "https://loteriascaixa-api.herokuapp.com/api/megasena/latest"
    resposta = requests.get(url)
    dados = resposta.json()
    numeros = dados["dezenas"]
    concurso = dados["concurso"]
    texto_resultado.config(text=f"Mega Sena\nConcurso {concurso}\n" + " - ".join(numeros),
                           bg="green",fg="white")

def buscar_quina():
    url="https://loteriascaixa-api.herokuapp.com/api/quina/latest"
    resposta= requests.get(url)
    dados = resposta.json()
    numeros = dados["dezenas"]
    concurso = dados["concurso"]
    texto_resultado.config(text=f"Quina\nConcurso {concurso}\n" + " - ".join(numeros),
                           bg="blue",fg="white")

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

def tela_serviçosFinanceiros():
    mostrar_tela(tela_serviços)

def abrir_tela_resultados():
    mostrar_tela(tela_resultados)

def tela_validar_conta():
    mostrar_tela(tela_validar)

def validar_conta():
    if not agencia.get() or not numero_conta.get():
        print("Erro")
        return

    validar_agencia=int(agencia.get())
    validar_conta=int(numero_conta.get())
    print(validar_agencia)
    if validar_agencia == kaiky["agencia"] and validar_conta == kaiky["conta"]:
        abrir_tela_saque()
    else:
        print('error')

def abrir_tela_saque():
    mostrar_tela(tela_saque)

def abrir_tela_principal():
    mostrar_tela(tela_principal)

def atualizar_carrinho():
    for widget in frame_lista.winfo_children():
        widget.destroy()
    for i, item in enumerate(carrinho):
        linha = tk.Frame(frame_lista)
        linha.pack(fill="x", pady=5, padx=10)
        texto = tk.Label(linha,text=f'{item["nome"]} |  R${item["preco"]:.2f}',font=("Arial", 16),anchor="w")
        texto.pack(side="left")
        botao_remover = tk.Button(linha,text="—",font=("Arial", 14, "bold")
                                  ,bg="red",fg="white",command=lambda idx=i: remover_aposta(idx))
        botao_remover.pack(side="left")

        total = sum(item["preco"] for item in carrinho)
        label_total.config(text=f"Total: R$ {total:.2f}")

def remover_aposta(indice):
    carrinho.pop(indice)
    atualizar_carrinho()
    total = sum(item["preco"] for item in carrinho)
    label_total.config(text=f"Total: R$ {total:.2f}")

def abrir_tela_atendimento():
    atualizar_carrinho()
    mostrar_tela(tela_atendimento)

def cancelar_operação():
    mostrar_tela(tela_principal)

def validar(texto,total_algarismos):
    return texto == "" or (texto.isdigit() and len(texto) <= int(total_algarismos))

#JANELA
janela=tk.Tk()
janela.geometry('1920x1080')
janela.title('Sistema de Loterico Caixa')
janela.state('zoomed')
logo= tk.PhotoImage(file='Imagens/logo_caixa.png')
janela.iconphoto(True,logo)


validacao = janela.register(validar)

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

    #BOTÃO ATENDIMENTO
botao_atendimento=tk.Button(tela_principal, text='Atendimento',font=('Arial', 25, 'bold'),
                            bg='#69BCC7', fg='white'
                           ,bd=2, relief='solid',width=20,command=abrir_tela_atendimento)
botao_atendimento.place(relx=0.01, rely=0.4)

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

#TELA DE SERVIÇOS
tela_serviços=tk.Frame(janela)

#TELA DE VALIDAÇÃO
tela_validar=tk.Frame(janela)


texto=tk.Label(tela_validar, text="Agência")
texto.pack()
agencia=tk.Entry(tela_validar,validate='key',validatecommand=(validacao,"%P",4))
agencia.pack()
texto=tk.Label(tela_validar, text="Conta")
texto.pack()
numero_conta=tk.Entry(tela_validar,validate='key',validatecommand=(validacao,"%P",10))
numero_conta.pack()

    #BOTÃO SAQUE
botao_saque= tk.Button(tela_serviços, text=f'{"Saque":^15}', font=('Arial', 30, 'bold'),
                       command=tela_validar_conta, bg='#69BCC7', fg='white', bd=True, relief="solid")
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

texto_resultado = tk.Label(tela_resultados,font=('Arial', 20, 'bold'),justify='center')
texto_resultado.place(relx=0.48, rely=0.5, anchor='center')

    #BOTÃO RESULTADO DA MEGA SENA
botao_resultado_megaSena=tk.Button(tela_resultados, text='MEGA SENA', font=('Arial', 30, 'bold'),
                                   bg='green', fg='white', bd=True, relief="solid"
                                   ,width=10,command=buscar_megasena)
botao_resultado_megaSena.place(relx=0.2, rely=0.2)

    #BOTÃO RESULTADO DA LOTOFACIL
botao_resultado_lotofacil=tk.Button(tela_resultados, text='LOTOFACIL', font=('Arial', 30, 'bold'),
                                    bg='purple', fg='white', bd=True, relief="solid"
                                    ,width=10,command=buscar_lotofacil)
botao_resultado_lotofacil.place(relx=0.4, rely=0.2)

    #BOTÃO RESULTADO DA QUINA
botao_resultado_quina=tk.Button(tela_resultados, text='QUINA', font=('Arial', 30, 'bold'),
                                bg='blue', fg='white', bd=True, relief="solid",
                                width=10,command=buscar_quina)
botao_resultado_quina.place(relx=0.6, rely=0.2)


    #BOTÃO VOLTAR (tela resultados)
botao_voltar=tk.Button(tela_resultados, text='Voltar', font=('Arial', 30, 'bold'),
                       command=abrir_tela_principal,bd=2, relief="solid")
botao_voltar.place(relx=0.01, rely=0.9)

#TELA DE ATENDIMENTO

tela_atendimento=tk.Frame(janela)

texto = tk.Label(tela_atendimento, font=("Arial", 16))
texto.pack()
label_total = tk.Label(tela_atendimento, font=("Arial", 18, "bold"))
label_total.pack()

frame_lista = tk.Frame(tela_atendimento)
frame_lista.pack(pady=20, fill="both", expand=True)

botao_voltar = tk.Button(tela_atendimento, text='X', font=('Arial', 30, 'bold'),
                             command=abrir_tela_principal, bd=2, relief="solid")



botao_voltar=tk.Button(tela_atendimento, text='Voltar', font=('Arial', 30, 'bold'),
                       command=abrir_tela_principal,bd=2, relief="solid")
botao_voltar.place(relx=0.01, rely=0.9)

#TELA DE SAQUE
tela_saque=tk.Frame(janela)

    #BOTÃO CANCELAR
botao_cancelar=tk.Button(tela_saque, text='Cancelar', font=('Arial', 30, 'bold'),
                         bg='red',fg='white',command=cancelar_operação,bd=2, relief="solid")
botao_cancelar.place(relx=0.01, rely=0.9)

    #BOTÃO CONFIRMAR
botao_confirmar=tk.Button(tela_validar,text='Confimar', font=('Arial', 30, 'bold'),
                          bg='green',fg='white',bd=2, relief="solid",command=validar_conta)
botao_confirmar.place(relx=0.87, rely=0.9)

texto_valor=tk.Label(tela_saque, text='Digite o valor \nMin: 5,00 | Max: 5.000,00', font=('Arial', 10, 'bold'))
texto_valor.place(relx=0.45,rely=0.45)
valor_saque=tk.Entry(tela_saque)
valor_saque.place(relx=0.45,rely=0.5)

janela.mainloop()