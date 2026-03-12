salario = 2000

# Variável global: pode ser acessada e modificada dentro da função usando a palavra-chave global.
# Não é recomendado usar variáveis globais, pois pode levar a código difícil de entender e manter.
def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario


salario_bonus(500)  # 2500
