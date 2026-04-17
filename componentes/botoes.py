import tkinter as tk

def botao_padrao(master, texto, comando, x, y, cor="#69BCC7", largura=20):
    btn = tk.Button(
        master,
        text=texto,
        command=comando,
        font=("Arial", 25, "bold"),
        bg=cor,
        fg="white",
        width=largura,
        bd=2,
        relief="solid"
    )
    btn.place(relx=x, rely=y)
    return btn