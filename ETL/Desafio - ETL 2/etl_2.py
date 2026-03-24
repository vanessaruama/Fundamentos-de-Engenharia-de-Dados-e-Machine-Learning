#Praticando Fundamentos de ETL com Python
# Desafio
# Você faz parte do time de tecnologia de uma empresa que desenvolve sistemas 
# para otimizar a gestão de milhares de negócios. Seu desafio é criar uma 
# solução simples de ETL (Extract, Transform, Load) para automatizar o 
# processamento de dados de vendas enviados por parceiros. Cada linha 
# recebida contém o nome do produto, a quantidade vendida e o valor unitário, 
# separados por vírgulas. Seu sistema precisa extrair esses dados, calcular 
# o valor total da venda (quantidade multiplicada pelo valor unitário) e 
# gerar uma string formatada para facilitar a integração com outros sistemas internos. 
# Essa automação tornará os processos empresariais mais eficientes, escaláveis e 
# inteligentes, reduzindo erros manuais e acelerando a tomada de decisão.

# Implemente um programa que leia uma linha contendo o nome do produto, 
# a quantidade vendida e o valor unitário, separados por vírgulas. 
# O programa deve calcular o valor total da venda (quantidade * valor unitário, 
# ambos inteiros) e retornar uma string no formato: "produto: total". Não utilize 
# bibliotecas externas, apenas recursos padrão da linguagem.

# Entrada
# Uma única linha contendo três valores separados por vírgula: o nome do produto (string),
# a quantidade vendida (inteiro) e o valor unitário (inteiro).

# Saída
# Uma única linha no formato "produto: total", onde produto é o nome do produto e 
# total é o valor total da venda (quantidade multiplicada pelo valor unitário).

# Leitura da linha de entrada
entrada = input().strip().split(',')
produto = entrada[0]
quantidade = int(entrada[1])
valor_unitario = int(entrada[2])
total = quantidade * valor_unitario

# TODO: Separe os campos da entrada e calcule o valor total da venda (quantidade * valor unitário)
# Dica: Use split(',') para separar os valores e int() para converter para inteiro

print(f"{produto}: {total}")  # Exemplo de saída formatada