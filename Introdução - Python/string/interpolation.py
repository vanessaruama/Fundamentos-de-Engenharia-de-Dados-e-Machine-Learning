nome = "Vanessa"
idade = 29
profissao = "Desenvolvedora"
linguagem = "Python"

# Utilizando o formato de string com o método format()
print("Olá, me chamo {} e tenho {} anos. Sou {} e estou matriculada no curso de {}.".format(nome, idade, profissao, linguagem))

# Utilizando o formato de string com a posição dos argumentos dentro do método format()
print("Olá, me chamo {0} e tenho {1} anos. Sou {2} e estou matriculada no curso de {3}.".format(nome, idade, profissao, linguagem))

# Utilizando o formato de string com o nome das variáveis dentro do método format()
print(f"Olá, me chamo {nome} e tenho {idade} anos. Sou {profissao} e estou matriculada no curso de {linguagem}.")

PI = 3.14159

# Formata o valor de PI para 2 casas decimais
print(f"Valor de PI: {PI:.2f}") 

# Formata o valor de PI para 10 caracteres de largura, alinhado à direita e com 2 casas decimais
print(f"Valor de PI: {PI:10.2f}")

dados = {"nome": "Vanessa", "idade": 29, "profissao": "Desenvolvedora", "linguagem": "Python"}

# Utilizando o formato de string com o método format() e desempacotando o dicionário com ** para acessar os valores pelas chaves
print("Nome: {nome}, Idade: {idade}, Profissão: {profissao}, Linguagem: {linguagem}".format(**dados))