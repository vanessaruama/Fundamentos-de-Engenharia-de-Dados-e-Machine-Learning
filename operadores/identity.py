curso = "Curso de Python"
nome_curso = curso
saldo, limite = 200, 200

# Verifica se as variáveis saldo e limite são idênticas (apontam para o mesmo objeto)
print( curso is nome_curso )
print( saldo is limite )

# Verifica se as variáveis saldo e limite são idênticas com o operador is not
print(curso is not nome_curso)
