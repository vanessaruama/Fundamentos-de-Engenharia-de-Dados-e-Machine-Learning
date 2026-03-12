import sys

saldo = 2000.0
saque = float(input("Digite o valor do saque: "))

# Estrutura condicional simples
if saldo >= saque:
    print("Saque realizado com sucesso!")

if saldo < saque:
    print("Saldo insuficiente para realizar o saque.")

# Estrutura condicional composta
if saldo >= saque:
    print("Saque realizado com sucesso!")

else:
    print("Saldo insuficiente para realizar o saque.")

opcao = int(input("Informe uma opção: [1] Sacar\n[2] Extrato:\n"))

# Estrutura condicional encadeada
if opcao == 1:
    valor = float(input("Digite o valor do saque: "))
elif opcao == 2:
    print("Exibindo extrato...")
else:
    sys.exit("Opção inválida!")

# Operador ternário
status = "Sucesso" if saldo >= saque else "Falha"
print(f"Status do saque: {status}")
