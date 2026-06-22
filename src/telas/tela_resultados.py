import tkinter as tk
from src.servicos.loterias_api import *

def abrir_tela_resultados(mostrar_tela,tela):
    mostrar_tela(tela)

def criar_tela_resultados(janela,mostrar_tela):
    tela = tk.Frame(janela)
    texto_resultado = tk.Label(tela, font=('Arial', 20, 'bold'), justify='center')
    texto_resultado.place(relx=0.48, rely=0.5, anchor='center')


    botao_resultado_megaSena = tk.Button(tela, text='MEGA SENA', font=('Arial', 30, 'bold'),
                                         bg='green', fg='white', bd=True, relief="solid"
                                         , width=10, command=lambda: buscar_megasena(texto_resultado))
    botao_resultado_megaSena.place(relx=0.2, rely=0.2)


    botao_resultado_lotofacil = tk.Button(tela, text='LOTOFACIL', font=('Arial', 30, 'bold'),
                                          bg='purple', fg='white', bd=True, relief="solid"
                                          , width=10, command=lambda: buscar_lotofacil(texto_resultado))
    botao_resultado_lotofacil.place(relx=0.4, rely=0.2)


    botao_resultado_quina = tk.Button(tela, text='QUINA', font=('Arial', 30, 'bold'),
                                      bg='blue', fg='white', bd=True, relief="solid",
                                      width=10, command=lambda: buscar_quina(texto_resultado))
    botao_resultado_quina.place(relx=0.6, rely=0.2)


    botao_voltar = tk.Button(tela, text='Voltar', font=('Arial', 30, 'bold'),
                             command=lambda:mostrar_tela("principal"), bd=2, relief="solid")
    botao_voltar.place(relx=0.01, rely=0.9)

    return tela