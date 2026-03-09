def sacar(valor):
    saldo = 500

    if saldo >= valor:
        print("Saque realizado com sucesso!")


def depositar(valor):
    saldo = 500

    if valor > 0:
        print("Depósito realizado com sucesso!")


depositar(500)
sacar(1000)
sacar(200)