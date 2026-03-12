# Parâmetros somente por posição são definidos usando a barra (/) e o asterisco (*) na definição da função.
# Eles indicam que os parâmetros anteriores à barra devem ser passados apenas por posição, 
# ou seja, na ordem correta, e não podem ser nomeados.
def criar_carro(modelo, ano, placa, /, *, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)


criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")

# Esta inválido porque os parâmetros modelo, ano e placa são definidos como parâmetros somente por posição,
# ou seja, eles devem ser passados na ordem correta e não podem ser nomeados.
# criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")  # inválido
