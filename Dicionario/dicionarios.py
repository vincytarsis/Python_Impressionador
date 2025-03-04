# Exercício 1
# Crie um sistema de consulta de preços
# Seu sistema deve:
# - Pedir para o usuário o nome de um produto
# - Caso o produto exista na lista de produtos, o programa deve retornar o preço do produto como resposta
#        - Ex: O produto celular custa R$1500
# - Caso o produto não exista na lista de produtos, o programa deve printar uma mensagem para o usuário tentar novamente
""" precos = {"celular": 1500, "camera": 1000, "fone de ouvido": 800, "monitor": 2000}

produto_procurado = input("Digite o produto:")
produto_procurado = produto_procurado.lower()
if produto_procurado in precos:
    preco = precos[produto_procurado]
    print(f"O produto {produto_procurado} custa R${preco}")
else:
    print("Produto não encontrado, tente novamente")
 """
# Exercício 2
# Agora edite o programa anterior para fazer com que, caso não exista o produto, o programa pergunte se o usuário quer cadastrar o produto
# Se ele responder sim, o programa deve pedir o nome do produto e o preco do produto e cadastrar no dicionário de preços
# Em seguida do cadastro bem sucedido, o programa deve printar o dicionário de precos atualizado
""" precos = {"celular": 1500, "camera": 1000, "fone de ouvido": 800, "monitor": 2000}

produto_procurado = input("Digite o produto:")
produto_procurado = produto_procurado.lower()
if produto_procurado in precos:
    preco = precos[produto_procurado]
    print(f"O produto {produto_procurado} custa R${preco}")
else:
    print("Produto não encontrado, tente novamente")
    cadastrar_produto = input("Deseja cadastrar o produto? (Sim(s)/Não(n)):").lower()
    if cadastrar_produto == "s" or cadastrar_produto == "sim":
        nome_novo_produto = input("Digite o nome do produto a ser cadastrado:").lower()
        preco_novo_produto = int(input("Digite o preço do produto:"))
        precos[nome_novo_produto] = preco_novo_produto
        print("Produto cadastrado com sucesso!")
        print("Dicionário de preços atualizado:", precos)
    elif cadastrar_produto == "n" or cadastrar_produto == "não":
        print("Produto não cadastrado.")
    else:
        print("Resposta inválida. Produto não cadastrado.") """

# Exercício 3
# Dada a lista de preços de produtos, uma loja resolveu fazer um reajuste nos preços dos produtos. 
# calcule o novo valor dos produtos com base nas seguintes regras:
# Preços até 1.000 vão ter um reajuste de 10% (ou seja, o novo preço será 110% do preço atual)
# Preços até maiores que 1.000 até 2.000 vão ter reajuste de 15%
# Preços acima de 2.000 vão ter reajuste de 20%
""" precos = {"celular": 1500, "camera": 1000, "fone de ouvido": 800, "monitor": 3000}

novos_precos = {} # Cria um novo dicionário para armazenar os preços reajustados

for produto, preco in precos.items():
    if preco <= 1000:
        reajuste = 0.10 # 10%
    elif preco <= 2000: # preços maiores que 1000 e menores ou iguais a 2000
        reajuste = 0.15 # 15%
    else: # preços maiores que 2000
        reajuste = 0.20 # 20%
    novo_preco = preco * (1 + reajuste) # Calcula o novo preço
    novos_precos[produto] = f"{novo_preco:.2f}" # Adiciona o produto e o novo preço formatado ao novo dicionário

print("Preços originais:", precos)
print("Novos preços reajustados:", novos_precos) """

# Exercício 4
# Edite o programa antigo para ter os 2 dicionários, o de preços originais e o de novos preços
# Em seguida calcule o valor total de reajuste em R$ que teve entre a lista de produtos original e a lista final

""" precos_originais = {"celular": 1500, "camera": 1000, "fone de ouvido": 800, "monitor": 3000}

novos_precos = {} # Cria um novo dicionário para armazenar os preços reajustados
total_reajuste = 0 # Inicializa a variável para o valor total de reajuste

for produto, preco_original in precos_originais.items():
    if preco_original <= 1000:
        reajuste_percentual = 0.10 # 10%
    elif preco_original <= 2000: # preços maiores que 1000 e menores ou iguais a 2000
        reajuste_percentual = 0.15 # 15%
    else: # preços maiores que 2000
        reajuste_percentual = 0.20 # 20%
    novo_preco = preco_original * (1 + reajuste_percentual) # Calcula o novo preço
    novos_precos[produto] = f"{novo_preco:.2f}" # Adiciona o produto e o novo preço formatado ao novo dicionário
    reajuste_valor = novo_preco - preco_original # Calcula o valor do reajuste para este produto
    total_reajuste += reajuste_valor # Acumula o valor do reajuste no total

print("Preços originais:", precos_originais)
print("Novos preços reajustados:", novos_precos)
print(f"Valor total de reajuste em R$: R${total_reajuste:.2f}") # Imprime o valor total do reajuste formatado
 """
# Exercício 5
# Uma empresa está analisando os resultados de vendas do 1º semestre de 2022 e 2023
# Qual foi o % de crescimento de cada mês de 2023 em relação a 2022?
# Depois de calcular isso, calcule o valor total de crescimento de 2023 em relação a 2022

""" vendas_22 = {"jan": 15000, "fev": 15500, "mar": 14000, "abr": 16600, "mai": 16300, "jun": 17000}
vendas_23 = {"jan": 17000, "fev": 15000, "mar": 17500, "abr": 16900, "mai": 16000, "jun": 18500}

crescimentos_percentuais_mes = {} # Dicionário para armazenar os crescimentos percentuais de cada mês
crescimento_total_valor = 0 # Variável para acumular o crescimento total em valor

for mes in vendas_22: # Itera sobre os meses de 2022 (poderia ser 2023 também, pois os meses são os mesmos)
    venda_2022 = vendas_22[mes]
    venda_2023 = vendas_23[mes]

    crescimento_valor_mes = venda_2023 - venda_2022 # Calcula o crescimento em valor para o mês
    crescimento_percentual_mes = (crescimento_valor_mes / venda_2022) * 100 # Calcula o crescimento percentual

    crescimentos_percentuais_mes[mes] = f"{crescimento_percentual_mes:.2f}%" # Armazena o crescimento percentual formatado no dicionário
    crescimento_total_valor += crescimento_valor_mes # Acumula o crescimento em valor no total

print("Crescimento percentual de cada mês de 2023 em relação a 2022:")
for mes, percentual in crescimentos_percentuais_mes.items():
    print(f"{mes}: {percentual}")

print(f"\nValor total de crescimento de 2023 em relação a 2022: R${crescimento_total_valor:.2f}") """

# Exercício 6 - Desafio
# No final da reunião de apresentação dos números, seu chefe perguntou:
# E se nos meses de 2023 que a gente vendeu menos do que 2022 a gente tivesse pelo menos empatado com 2022 (ou seja, se nos meses de 2023 em que as vendas foram menores do que o mesmo mês em 2022, o valor de vendas tivesse sido igual a 2022)
# Qual teria sido o nosso crescimento de 2023 frente a 2022?

vendas_22 = {"jan": 15000, "fev": 15500, "mar": 14000, "abr": 16600, "mai": 16300, "jun": 17000}
vendas_23 = {"jan": 17000, "fev": 15000, "mar": 17500, "abr": 16900, "mai": 16000, "jun": 18500}

vendas_23_ajustadas = {} # Dicionário para armazenar as vendas de 2023 ajustadas
crescimento_total_valor_ajustado = 0 # Variável para acumular o crescimento total ajustado em valor

for mes in vendas_22:
    venda_2022 = vendas_22[mes]
    venda_2023 = vendas_23[mes]

    if venda_2023 < venda_2022:
        vendas_23_ajustadas[mes] = venda_2022 # Usa o valor de 2022 se venda de 2023 foi menor
    else:
        vendas_23_ajustadas[mes] = venda_2023 # Mantém o valor real de 2023 se foi maior ou igual

crescimento_total_valor_ajustado = sum(vendas_23_ajustadas.values()) - sum(vendas_22.values()) # Calcula o crescimento total ajustado em valor
crescimento_percentual_total_ajustado = (crescimento_total_valor_ajustado / sum(vendas_22.values())) * 100 # Calcula o crescimento percentual ajustado

print("Vendas de 2023 ajustadas (igual a 2022 se venda de 2023 foi menor):")
for mes, venda in vendas_23_ajustadas.items():
    print(f"{mes}: R${venda:.2f}")

print(f"\nValor total de crescimento de 2023 (ajustado) em relação a 2022: R${crescimento_total_valor_ajustado:.2f}")
print(f"Crescimento percentual total de 2023 (ajustado) em relação a 2022: {crescimento_percentual_total_ajustado:.2f}%")
