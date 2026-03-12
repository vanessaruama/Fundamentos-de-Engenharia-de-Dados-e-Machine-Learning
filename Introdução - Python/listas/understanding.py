numeros = [1, 30, 21, 2, 9, 12, 8, 15, 7, 10]
pares = []

# Comprensão de listas para criar uma nova lista com os números pares
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

print(pares)

# A mesma lógica usando compreensão de listas, 
# porém de forma mais concisa, sem a necessidade de criar uma lista vazia 
# e usar o método append()
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)

# Criando uma nova lista com o quadrado dos números usando compreensão de listas
quadrado = [numero ** 2 for numero in numeros]
print(quadrado)