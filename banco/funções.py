import sqlite3


conexao = sqlite3.connect('dados.db')

cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    idade INTEGER,
    agencia INTEGER,
    conta INTEGER,
    saldo INTEGER
)
""")




cursor.execute("UPDATE usuarios SET saldo = ? WHERE id = ?",
               (600,1))


conexao.commit()

cursor.execute("SELECT * FROM usuarios")

dados = cursor.fetchall()

print(dados)