def somar(a, b):
    return a + b


# Recebe a função somar como argumento e a executa dentro da função exibir_resultado.
def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação {a} + {b} = {resultado}")


exibir_resultado(10, 10, somar)  # O resultado da operação 10 + 10 = 20
