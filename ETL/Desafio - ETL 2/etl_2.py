# Desafio
# Você faz parte do time de tecnologia de uma empresa que
#  desenvolve sistemas para automatizar processos empresariais
#  em larga escala. Seu time está criando uma solução de ETL (Extract, Transform, Load)
#  para ajudar negócios a processar dados de clientes de forma eficiente e 
# inteligente. O objetivo é transformar informações brutas recebidas de 
# diferentes setores em dados padronizados, prontos para análise e tomada de decisão. 
# Para isso, você precisa criar um script que leia uma linha de dados extraída de 
# um sistema legado, realize uma transformação específica e devolva o resultado 
# pronto para ser carregado em um novo sistema. O sucesso dessa tarefa é fundamental 
# para garantir que os processos empresariais sejam mais ágeis, escaláveis e confiáveis.

# Implemente um programa que leia uma string contendo nomes de clientes separados 
# por vírgula e espaço. Seu programa deve transformar cada nome para letras maiúsculas, 
# remover espaços extras antes e depois de cada nome, e retornar os nomes transformados, 
# separados por ponto e vírgula e um espaço. Não utilize bibliotecas externas. 
# O formato de entrada e saída deve ser exatamente como especificado.

# Entrada
# Uma única linha contendo nomes de clientes separados por vírgula e espaço. 
# Os nomes podem conter espaços extras antes ou depois de cada nome.

# Saída
# Uma única linha com os nomes em letras maiúsculas, sem espaços extras, 
# separados por ponto e vírgula seguido de espaço.

# Lê a linha de entrada contendo nomes separados por vírgula e espaço
entrada = input()

# TODO: Para cada nome, remova espaços extras e transforme em maiúsculas
# Dica: Use split(',') para separar os nomes e depois aplique strip() e upper() em cada um
nomes = [nome.strip().upper() for nome in entrada.split(',')]
# Exemplo de saída esperada: 'ANA; BRUNO; CARLA'
print('; '.join(nomes))