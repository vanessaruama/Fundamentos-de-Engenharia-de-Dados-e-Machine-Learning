carros = ["gol", "celta", "palio", "uno"]

for carro in carros:
    print(carro)

# Acessando o índice e o valor do elemento via função enumerate() que retorna uma tupla com o índice e o valor do elemento
for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")