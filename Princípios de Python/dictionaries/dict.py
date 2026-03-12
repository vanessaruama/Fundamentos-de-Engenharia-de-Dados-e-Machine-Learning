# Métodos do dicionário

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "123456789"},
    "maria@gmail.com": {"nome": "Maria", "telefone": "987654321"},
    "joao@gmail.com": {"nome": "João", "telefone": "555555555", "extra": {"a": 1}}
}

contatos.clear()  # Limpa o dicionário, removendo todos os pares chave-valor
print(contatos)  # Saída: {}

# ******************************************************************************
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "123456789"}
}

contatos_copy = contatos.copy()  # Cria uma cópia rasa do dicionário
print(contatos_copy)

# ******************************************************************************
# O fromkeys é um método de classe que cria um novo dicionário a partir de uma sequência de chaves, 
# atribuindo a cada chave um valor específico.
print(dict.fromkeys(["nome", "telefone"]))  # Cria um dicionário com as chaves "nome" e "telefone", todas com valor None
print(dict.fromkeys(["nome", "telefone"], "default"))  # Cria um dicionário com as chaves "nome" e "telefone", todas com valor "default"

# ******************************************************************************
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "123456789"}
}

print(contatos.get("chave"))  # Retorna None, pois a chave "chave" não existe no dicionário
print(contatos.get("chave", "Valor padrão"))  # Retorna "Valor padrão", pois a chave "chave" não existe no dicionário
print(contatos.get("guilherme@gmail.com"))  # Retorna o valor associado à chave "guilherme@gmail.com"

# ******************************************************************************
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "123456789"}
}

print(contatos.items())  # Retorna uma visão dos itens do dicionário como pares chave-valor
print(contatos.keys())  # Retorna uma visão das chaves do dicionário
print(contatos.values())  # Retorna uma visão dos valores do dicionário
print(contatos.pop("guilherme@gmail.com"))  # Remove e retorna o valor associado à chave "guilherme@gmail.com"

# ******************************************************************************
contato = {"nome": "Guilherme", "telefone": "123456789"}

contato.setdefault("email", "default@example.com")  # Adiciona a chave "email" com o valor "default@example.com" se ela não existir
print(contato)

# ******************************************************************************
contato = {"nome": "Guilherme", "telefone": "123456789"}

contato.update({"telefone": "987654321", "email": "guilherme@example.com"}) # Atualiza o valor da chave "telefone" e adiciona a chave "email"
print(contato)

# ******************************************************************************
contato = {"guilherme@example.com": {"nome": "Guilherme", "telefone": "123456789"}}

print("guilherme@gmail.com" in contato) # Verifica se a chave "guilherme@gmail.com" existe no dicionário
print("guilherme@example.com" in contato)

print("nome" in contato["guilherme@example.com"]) # Verifica se a chave "nome" existe no dicionário associado à chave "guilherme@example.com"

# ******************************************************************************
contato = {
    "guilherme@example.com": {"nome": "Guilherme", "telefone": "123456789"},
    "maria@example.com": {"nome": "Maria", "telefone": "987654321"}
    }

del contato["guilherme@example.com"]["telefone"]  # Remove a chave "telefone" do dicionário associado à chave "
print(contato)

del contato["maria@example.com"]
print(contato)