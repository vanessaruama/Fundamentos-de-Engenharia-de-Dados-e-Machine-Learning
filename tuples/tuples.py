#Tuplas são imutáveis, ou seja, não podem ser alteradas depois de criadas. 
# Elas são definidas usando parênteses () e podem conter elementos de diferentes tipos de dados.

#boa prática usar vírgula no final da tupla, mesmo que tenha apenas um elemento, para evitar confusão com parênteses normais.
frutas = ("maçã", "banana", "laranja",)
print(frutas)

letras = tuple("python")
print(letras)

numeros = tuple([1, 2, 3, 4, 5])
print(numeros)

pais = ("Brasil",)
print(pais)  

tuplas = ("p", "y", "t", "h", "o", "n",)
print(tuplas)
print(tuplas[2:])
print(tuplas[:2])
