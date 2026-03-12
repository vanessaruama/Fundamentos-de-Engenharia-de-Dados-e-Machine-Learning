# Um dicionário é um conjunto não-ordenado de pares chave-valor. 
# Ele é mutável, o que significa que pode ser alterado após a criação. 
# Os dicionários são definidos usando chaves {} e os pares chave-valor são separados por dois pontos (:).

pessoa = {"nome": "João", "idade": 30, "cidade": "São Paulo"}

# O dict é uma função construtora que pode ser usada para criar um dicionário a partir de uma sequência de pares chave-valor.
pessoa = dict(nome="João", idade=30, cidade="São Paulo")
print(pessoa)

# Adicionando um novo par chave-valor ao dicionário
pessoa["telefone"] = "123456789"
print(pessoa)

# Acessando o valor associado à chave "nome"
print(pessoa["nome"])  

# *****************************************************************************
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "123456789"},
    "maria@gmail.com": {"nome": "Maria", "telefone": "987654321"},
    "joao@gmail.com": {"nome": "João", "telefone": "555555555", "extra": {"a": 1}}
}

print(contatos["guilherme@gmail.com"])
print(contatos["guilherme@gmail.com"]["telefone"])
print(contatos["joao@gmail.com"]["extra"])
print(contatos["joao@gmail.com"]["extra"]["a"])

# *****************************************************************************
for chave in contatos:
    print(chave, contatos[chave])
    print(chave, contatos[chave]["nome"])