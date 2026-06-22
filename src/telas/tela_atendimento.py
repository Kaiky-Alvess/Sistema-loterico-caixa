import tkinter as tk

def criar_tela_atendimento(janela, mostrar_tela):
    tela = tk.Frame(janela)

    texto = tk.Label(tela, font=("Arial", 16))
    texto.pack()

    label_total = tk.Label(tela, font=("Arial", 18, "bold"))
    label_total.pack()

    frame_lista = tk.Frame(tela)
    frame_lista.pack(pady=20, fill="both", expand=True)

    botao_ver_jogos = tk.Button(tela, text='Ver Jogos', font=('Arial', 30, 'bold'),
                                bd=2, relief="solid",
                                command=lambda: mostrar_tela("jogos"))
    botao_ver_jogos.place(relx=0.5, rely=0.9, anchor='center')

    botao_finalizar = tk.Button(tela, text='Finalizar', font=('Arial', 30, 'bold'),
                                command=lambda:mostrar_tela("confirmar_deposito")
                                , bd=2, relief="solid")
    botao_finalizar.place(relx=0.89, rely=0.9)

    botao_voltar = tk.Button(tela, text='Voltar', font=('Arial', 30, 'bold'),
                             command=lambda:mostrar_tela("principal"), bd=2, relief="solid")
    botao_voltar.place(relx=0.01, rely=0.9)
    return tela