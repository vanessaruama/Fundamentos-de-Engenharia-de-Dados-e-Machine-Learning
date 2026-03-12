# Set é uma coleção de elementos únicos e não ordenados. 
# Ele é definido usando chaves {} e pode conter elementos de diferentes tipos de dados.
# Conjuntos não tem indexação, ou seja, não é possível acessar os elementos por posição. 
# Para isso precisa converter o set para uma lista ou tupla.

print(set([1, 2, 3, 4, 5, 4, 2]))

print(set("abacaxi"))

# Passando uma tupla para o set e ele irá criar um set com os elementos únicos da tupla.
print(set(("palio", "gol", "celta", "palio")))

# Outra forma de criar um set é usando {} e separando os elementos por vírgula.
linguagens = {"python", "java", "c++", "python"}
print(linguagens)

# *******************************************************************************************
numero = {1, 2, 3, 3, 2}

# Convertendo o set para uma lista para acessar os elementos por posição.
numero = list(numero)
print(numero[1])

# *******************************************************************************************
carros = {"palio", "gol", "celta", "palio"}

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

# *******************************************************************************************
conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {4, 5, 6, 7, 8}

# União dos conjuntos
print(conjunto_a.union(conjunto_b))

# Interseção dos conjuntos
print(conjunto_a.intersection(conjunto_b))

# Elementos que estão no conjunto_a mas não estão no conjunto_b)
print(conjunto_a.difference(conjunto_b)) 

# Elementos que estão em um dos conjuntos, mas não em ambos.
print(conjunto_a.symmetric_difference(conjunto_b)) 

# Verifica se o conjunto_a é um subconjunto do conjunto_b
print(conjunto_a.issubset(conjunto_b)) 

# Verifica se o conjunto_a é um superconjunto do conjunto_b
print(conjunto_a.issuperset(conjunto_b)) 

# Verifica se os conjuntos não possuem elementos em comum. 
# Retorna True se os conjuntos forem disjuntos, ou seja, não tiverem elementos em comum, e 
# False caso contrário.
print(conjunto_a.isdisjoint(conjunto_b)) 

# *******************************************************************************************
sorteio = {1, 23}

sorteio.add(45)
sorteio.add(22)
# Não adiciona o elemento 23, pois ele já existe no set.
sorteio.add(23)
print(sorteio)

# *******************************************************************************************
sorteio = {1, 23, 45, 22}

print(sorteio)
sorteio.clear()
print(sorteio)

# *******************************************************************************************
sorteio = {1, 23, 45, 22}

sorteio_copy = sorteio.copy()
print(sorteio_copy)

# *******************************************************************************************
numeros = {1, 2, 3, 4, 5, 1, 2}

numeros.discard(3)
print(numeros)

# *******************************************************************************************
numeros = {1, 2, 3, 4, 5, 1, 2}

print(len(numeros))
numeros.pop()
numeros.pop()
print(numeros)