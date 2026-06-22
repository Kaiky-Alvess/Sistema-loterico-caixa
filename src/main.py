from src.telas import tela_principal
from src.telas.tela_conta_criada import *
from src.telas.tela_atendimento import criar_tela_atendimento
from src.telas.tela_confirmar_deposito import *
from src.telas.tela_deposito import *
from src.telas.tela_jogos import *
from src.telas.tela_principal import criar_tela_principal
from src.telas.tela_saldo import *
from src.telas.tela_saque import *
from src.telas.tela_serviços import *
from src.telas.tela_validar import *
from telas.tela_resultados import *
from loterias.loterias import *
from src.telas.tela_criar_conta import *
from banco.classe import *


banco.listar_contas()

carrinho=[]

conta_atual=0

saque_ou_deposito= ''

jogos=['LOTOFACIL','MEGASENA', 'QUINA']

precos = {"Mega Sena": 6.00,"Lotofacil": 3.50,"Quina": 3.00}

telas= {}

tela_atual = None

def mostrar_tela(nome):
    global tela_atual
    if tela_atual is not None:
        tela_atual.pack_forget()
    telas[nome].pack(fill='both', expand=True)
    tela_atual = telas[nome]

def pegar_operacao():
    return saque_ou_deposito


def calcular_carrinho():
    total = sum(item["preco"] for item in carrinho)
    label_total.config(text=f"Total: R$ {total:.2f}")

def finalizar_atendimento():
    carrinho.clear()
    atualizar_carrinho()
    calcular_carrinho()
    mostrar_tela(tela_principal)

def abrir_tela_principal():
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


def validar_num(texto,total_algarismos):
    return texto == "" or (texto.isdigit() and len(texto) <= int(total_algarismos))

def validar_txt(texto_inserido):
    return not any(char.isdigit() for char in texto_inserido)

def definir_conta_atual(id_conta):
    global conta_atual
    conta_atual = id_conta

def pegar_conta_atual():
    return conta_atual


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
telas["principal"]=criar_tela_principal(janela,mostrar_tela)

telas["atendimento"]=criar_tela_atendimento(janela,mostrar_tela)

telas["conta_criada"],informacoes=criar_tela_conta_criada(janela,mostrar_tela)

telas["criar_conta"]= criar_tela_criar_conta(janela,mostrar_tela,
                                         valida_texto,valida_num,informacoes)

#TELA DE VALIDAÇÃO
telas["validar"]= criar_tela_validar(janela, mostrar_tela, valida_num,pegar_operacao,definir_conta_atual)

#TELA SERVIÇOS FINANCEIROS
telas["servicos_financeiros"]=criar_tela_serviços_financeiros(janela,mostrar_tela)

#TELA DE RESULTADOS
telas["resultados"]=criar_tela_resultados(janela,mostrar_tela)


#TELA DE ATENDIMENTO

telas["mega_sena"] = criar_tela_loteria(janela, mostrar_tela, "Mega Sena", 60, 6, 10,
                                         "green", "#DAA520", carrinho, precos["Mega Sena"])

telas["lotofacil"] = criar_tela_loteria(janela, mostrar_tela, "Lotofacil", 25, 15, 5,
                                          "purple", "#DAA520", carrinho, precos["Lotofacil"])

telas["quina"] = criar_tela_loteria(janela,mostrar_tela, "Quina", 80, 5, 10,
                                  "blue", "#DAA520", carrinho, precos["Quina"])

telas["saque"]=criar_tela_saque(janela,mostrar_tela,valida_num,carrinho,pegar_conta_atual)

telas["deposito"]=criar_tela_deposito(janela,mostrar_tela,carrinho,pegar_conta_atual)

telas["confirmar_deposito"]=criar_tela_confirmar_deposito(janela,mostrar_tela,carrinho,
                                                      finalizar_atendimento)

telas["saldo"]=criar_tela_saldo(janela,mostrar_tela,pegar_conta_atual,valida_num)

telas["jogos"]=criar_tela_jogos(janela,mostrar_tela)

mostrar_tela("principal")
janela.mainloop()