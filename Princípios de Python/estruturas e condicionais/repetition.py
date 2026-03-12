texto = input("Digite um texto: ")
VOGAIS = "AEIOU"

# Estrutura de repetição for para percorrer cada letra do texto
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end=" ")

else:
    print()


# range(stop) -> range object
# range (start, stop[, step]) -> range object

# Está função gera uma sequência de números, começando do 0 (padrão) até o número especificado (exclusive)
print(list(range(4))) # range(0, 4) -> 0, 1, 2, 3

# Utilizando o range com start e stop
for numero in range(0, 11):
    print(numero, end=" ")
    print("\n")

#Utilizando o range com start, stop e step, o step é o incremento, ou seja, o valor que será adicionado a cada iteração
for numero in range(0, 51, 5):
    print(numero, end=" ")

opcao = -1

# Estrutura de repetição while para exibir um menu de opções
while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n:"))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo extrato...")
else:
    print("Obrigado por usar nosso sistema bancário, até logo!")

# Estrutura de repetição com uso do break para sair do loop quando um número específico for encontrado
while True:
    numero = int(input("Digite um número: "))

    if numero == 10:
        print("Número 10 encontrado, saindo do loop.")
        break

    print(numero, end=" ")
    print("\n")

# Estrutura de while usando o continue para pular a iteração quando um número específico for encontrado
while True:
    numero = int(input("Digite um número: "))

    if numero == 10:
        print("Número 10 encontrado, pulando a iteração.")
        continue

    print(numero, end=" ")
    print("\n")