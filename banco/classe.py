import sqlite3
import os
from random import randint


CAMINHO_DB = os.path.join(
    os.path.dirname(__file__),
    'dados.db'
)


class Conta():
    def __init__(self, titular, saldo=0,id=None,tipo=None,conta=None,senha=None):
        self.id=id
        self.titular = titular
        self.saldo = saldo
        self.agencia = 732
        self.conta = conta or randint(100000,999999)
        self.senha= senha or randint(1000,9999)
        self.tipo = tipo
    def depositar(self, valor):
        if valor > 0 and valor < 5000:
            self.saldo += valor
            return f'Depósito de R${valor:.2f} realizado com sucesso.'
        else:
            return 'Valor de depósito inválido.'

    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo and valor <= 5000:
            self.saldo -= valor
            return f'Saque de R${valor:.2f} realizado com sucesso.'
        else:
            return 'Saldo insuficiente ou valor inválido.'
    def __str__(self):
        return f'Conta de {self.titular} com saldo de R${self.saldo:.2f}'


class ContaPoupanca(Conta):
    def __init__(self, titular, saldo=0 ):
        super().__init__(titular, saldo)
        self.tipo = 'Poupanca'
    def render_juros(self):
        if self.saldo > 0:
            juros = self.saldo * 0.01
            self.saldo += juros
            return f'Juros de R${juros:.2f} renderizados com sucesso.'
        else:
            return 'Saldo insuficiente para render juros.'




class ContaCorrente(Conta):
    def __init__(self, titular, saldo=0):
        super().__init__(titular, saldo)
        self.tipo = 'Corrente'
    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo and valor <= 5000:
            if valor < 500:
                taxa = 0
                self.saldo -= (valor + taxa)
                return f'Saque de R${valor:.2f} realizado com sucesso. Taxa de R${taxa:.2f} aplicada.'
            else:
                self.saldo -= valor
            return f'Saque de R${valor:.2f} realizado com sucesso.'
        else:
            return 'Saldo insuficiente ou valor inválido.'

class Banco():
    def __init__(self):
        self.conexao = sqlite3.connect(CAMINHO_DB)
        self.cursor=self.conexao.cursor()
        self.criar_tabela()

    def criar_tabela(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            saldo REAL,
            agencia INTEGER,
            conta INTEGER,
            tipo TEXT,
            senha TEXT
        )
        """)
        self.conexao.commit()

    def salvar_conta(self, conta):
        self.cursor.execute("""
        INSERT INTO usuarios (nome, saldo,  agencia, conta ,tipo, senha)
        VALUES (?, ?, ?, ?, ?, ?)
        """, (conta.titular, conta.saldo, conta.agencia, conta.conta, conta.tipo, conta.senha))

        self.conexao.commit()

    def listar_contas(self):
        self.cursor.execute("""
        SELECT * FROM usuarios
        """)

        dados = self.cursor.fetchall()
        contas = []

        for dado in dados:
            conta = Conta(
                titular=dado[1],
                saldo=dado[2],
                id=dado[0],
                tipo=dado[5]
            )
            conta.agencia = dado[3]
            conta.conta = dado[4]
            conta.senha=dado[6]
            contas.append(conta)
        return contas

    def atualizar_conta(self, conta):
        self.cursor.execute("""
        UPDATE usuarios
        SET nome = ?, saldo = ?, agencia = ?, conta = ?, tipo = ?, senha = ?
        WHERE id = ?
        """, (
            conta.titular,
            conta.saldo,
            conta.agencia,
            conta.conta,
            conta.tipo,
            conta.senha,
            conta.id,

        ))

        self.conexao.commit()

    def buscar_conta(self, id):
        self.cursor.execute("""
        SELECT * FROM usuarios
        WHERE id = ?
        """, (id,))

        dado = self.cursor.fetchone()
        if dado is None:
            print("Conta não encontrada")
            return None

        if dado[5] == 'Poupanca':
            conta = ContaPoupanca(
                titular=dado[1],
                saldo=dado[2]
            )
        else:
            conta = ContaCorrente(
                titular=dado[1],
                saldo=dado[2]
            )
        conta.id=dado[0]
        conta.agencia = dado[3]
        conta.conta = dado[4]
        conta.senha = dado[6]

        return conta

banco=Banco()
if __name__ == '__main__':
    contas=banco.listar_contas()
    for conta in contas:
        print(conta.titular)
        print(conta.saldo)
        print(conta.agencia)
        print(conta.conta)
        print(conta.tipo)
        print(conta.senha)

