class Conta():
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            return f'Depósito de R${valor:.2f} realizado com sucesso.'
        else:
            return 'Valor de depósito inválido.'

    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            return f'Saque de R${valor:.2f} realizado com sucesso.'
        else:
            return 'Saldo insuficiente ou valor inválido.'

    def tipo(self):
        return 'Conta'

    def __str__(self):
        return f'Conta de {self.titular} com saldo de R${self.saldo:.2f}'


class ContaPoupanca(Conta):
    def __init__(self, titular, saldo=0):
        super().__init__(titular, saldo)

    def render_juros(self):
        if self.saldo > 0:
            juros = self.saldo * 0.01
            self.saldo += juros
            return f'Juros de R${juros:.2f} renderizados com sucesso.'
        else:
            return 'Saldo insuficiente para render juros.'

    def tipo(self):
        return 'Conta Poupança'


class ContaCorrente(Conta):
    def __init__(self, titular, saldo=0):
        super().__init__(titular, saldo)

    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            if valor < 500:
                taxa = 1
                self.saldo -= (valor + taxa)
                return f'Saque de R${valor:.2f} realizado com sucesso. Taxa de R${taxa:.2f} aplicada.'
            else:
                self.saldo -= valor
            return f'Saque de R${valor:.2f} realizado com sucesso.'
        else:
            return 'Saldo insuficiente ou valor inválido.'

    def tipo(self):
        return 'Conta Corrente'