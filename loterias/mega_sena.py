import tkinter as tk

selecionados = []

def marcar(numero, botao):
    if numero in selecionados:
        selecionados.remove(numero)
        botao.config(bg="white", fg="black")
    else:
        if len(selecionados) < 6:
            selecionados.append(numero)
            botao.config(bg="green", fg="white")

def criar_tela_megasena(janela):
    frame = tk.Frame(janela)

    # área central
    area = tk.Frame(frame)
    area.pack(expand=True)

    for i in range(1, 61):
        botao = tk.Button(
            area,
            text=f"{i:02}",
            width=5,
            height=2,
            font=("Arial", 14, "bold")
        )

        botao.config(command=lambda n=i, b=botao: marcar(n, b))

        linha = (i - 1) // 10
        coluna = (i - 1) % 10

        botao.grid(row=linha, column=coluna, padx=6, pady=6)

    return frame