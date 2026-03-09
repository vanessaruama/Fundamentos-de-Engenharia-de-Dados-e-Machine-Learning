saldo = 1000
saque = 200
limite = 100
conta_especial = True

# Operador lógico AND, verifica se ambas as condições são verdadeiras
print(saldo >= saque and saque <= limite)

# Operador lógico OR, verifica se pelo menos uma das condições é verdadeira
print(saldo >= saque or saque <= limite)

# Operador lógico NOT, inverte o resultado da condição
print(not saldo >= saque)

contatos_emergencia = []

# Verifica se a lista de contatos de emergência está vazia usando o operador NOT
print(not contatos_emergencia)

# Exemplo de uso do operador NOT com uma string
print(not "saque 1500;")

# Exemplo de uso do operador NOT com uma string vazia
print(not "")

# Combinação de operadores lógicos
print(saldo >= saque and saque <= limite or conta_especial and saldo >= saque)

# Uso de parênteses para controlar a ordem de avaliação dos operadores lógicos
print((saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque))