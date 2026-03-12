lista = []

# Utilizando o método append() para adicionar elementos à lista
lista.append(1)
lista.append("Python")
lista.append([40, 30, 20])

print(lista)
#======================================================================#
# Limpando a lista
lista.clear()  
print(lista)

#=====================================================================#
lista = [1, "Python", [40, 30, 20]]
# Criando uma cópia da lista usando o método copy()
lista_copiada = lista.copy()
print(lista_copiada)

#=====================================================================#
cores = ["vermelho", "verde", "azul"]

# Retorna o número de vezes que "verde" aparece na lista
print(cores.count("verde"))
# Retorna 0, pois "amarelo" não está na lista   
print(cores.count("amarelo"))
# Retorna 1, pois "vermelho" aparece uma vez na lista    
print(cores.count("vermelho"))  

#=====================================================================#
linguagens = ["Java", "C++", "Python", "JavaScript"]
print(linguagens)
# Utiliza o extend() para adicionar os elementos de outra lista à lista original
linguagens.extend(["Go", "Rust"])

print(linguagens)

#=====================================================================#
linguagens = ["Java", "C++", "Python", "JavaScript"]
# Retorna o índice da primeira ocorrência de "Python"
print(linguagens.index("Python")) 
# Retorna o índice de "Java" 
print(linguagens.index("Java"))    

#=====================================================================#
linguagens = ["Java", "C++", "Python", "JavaScript"]

# Remove o último elemento da lista e o retorna
print(linguagens.pop())
print(linguagens.pop())
print(linguagens.pop())
print(linguagens.pop(0))
print(linguagens)

#=====================================================================#
linguagens = ["Java", "C++", "Python", "JavaScript"]
# Remove "C++" da lista
linguagens.remove("C++")
print(linguagens)

#=====================================================================#
linguagens = ["Java", "C++", "Python", "JavaScript"]
# Inverte a ordem dos elementos da lista
linguagens.reverse()
print(linguagens)

#=====================================================================#
linguagens = ["Java", "C++", "Python", "JavaScript"]
# Ordena os elementos da lista em ordem alfabética
linguagens.sort()
print(linguagens)

linguagens = ["Java", "C++", "Python", "JavaScript"]
# Ordena em ordem alfabética reversa
linguagens.sort(reverse=True)  

linguagens = ["Java", "C++", "Python", "JavaScript"]
# Ordena pela quantidade de caracteres
linguagens.sort(key=lambda x: len(x))  
print(linguagens)

# Ordena pela quantidade de caracteres em ordem reversa
linguagens.sort(key=lambda x: len(x), reverse=True)  
print(linguagens)

#=====================================================================#
linguagens = ["Java", "C++", "Python", "JavaScript"]
# Retorna o número de elementos na lista
print(len(linguagens))

#=====================================================================#
linguagens = ["Java", "C++", "Python", "JavaScript"]
# Sorted() utilizado para ordenar a lista sem modificar a original
print(sorted(linguagens, key=lambda x: len(x)))
# Sorted() com reverse=True para ordenar em ordem reversa
print(sorted(linguagens, key=lambda x: len(x), reverse=True))