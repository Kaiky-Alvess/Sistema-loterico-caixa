from src.banco.classe import *

def criar_conta(titular,senha,tipo,label,mostrar_tela):
    if titular and int(senha) and len(senha) == 4:
        if tipo=='Poupança':
            conta=(ContaPoupanca(titular=str(titular),senha=int(senha)))
            pass
        else:
            conta=(ContaCorrente(titular=str(titular),senha=int(senha)))
        banco.salvar_conta(conta)
        label.config(text=f'Titular: {conta.titular}\n'
f'Agencia: {conta.agencia}\n'
f'Conta: {conta.conta}\n'
f'Tipo: {conta.tipo}\n'
f'Senha: {conta.senha}\n',anchor="e")


