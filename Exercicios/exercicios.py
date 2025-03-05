#!/usr/bin/env python
# coding: utf-8

# # Exercícios de fixação 

# A seguir, você encontrará alguns exercícios para fixar os conceitos aprendidos no curso até agora. Os exercícios estão divididos por exemplos práticos da vida real:
# 
# - lista de compras
# - previsão de vendas
# - relatório de vendas
# - segmentação de clientes
# - analisador de texto
# 
# Para cada assunto, você encontrará ao menos um exercício. Nos casos onde há mais de um exercício para o mesmo assunto, você será convidado a resolver o mesmo problema de formas diferentes. Isso é proposital, pois o objetivo é que você pratique o que aprendeu e, ao mesmo tempo, aprenda novas formas de resolver um mesmo problema. Por exemplo, usando diferentes estruturas de dados, ou diferentes formas de iterar sobre uma estrutura de dados, ou, ainda, utilizando funções.
# 
# Tente resolver os exercícios sozinho. Se tiver dificuldades, consulte o material do curso e, se ainda assim não conseguir resolver, consulte a solução.

# ## Lista de compras

# ### Primeira versão da lista de compras

# Escreva um programa que permita que um usuário crie uma lista de compras.
# O usuário deve ser capaz de adicionar itens, remover itens e visualizar a lista.
# 
# Estruture seu programa da seguinte forma:
# 
# 1. Crie uma lista vazia para armazenar os itens da lista de compras.
# 2. Crie um loop infinito que imprima um menu de opções ao usuário e permita que ele escolha uma opção.
# 3. Dentro do loop, use uma declaração if para executar a tarefa apropriada de acordo com a escolha do usuário.
# 4. Se o usuário escolher adicionar um item, solicite que ele digite o nome do item e adicione-o à lista.
# 5. Se o usuário escolher remover um item, solicite que ele digite o nome do item e remova-o da lista.
# 6. Se o usuário escolher ver a lista, mostre cada item da lista em sua própria linha.
# 7. Se o usuário escolher sair, encerre o loop usando break.
# 
# Exemplo de saída:
# 
# ```
# 1 Adicionar item
# 2 Remover item
# 3 Ver lista
# 4 Sair
# Escolha uma opção: 1
# Digite um item: banana
# 
# 1 Adicionar item
# 2 Remover item
# 3 Ver lista
# 4 Sair
# Escolha uma opção: 1
# Digite um item: maçã
# 
# 1 Adicionar item
# 2 Remover item
# 3 Ver lista
# 4 Sair
# Escolha uma opção: 3
# ['banana', 'maçã']
# 
# 1 Adicionar item
# 2 Remover item
# 3 Ver lista
# 4 Sair
# Escolha uma opção: 2
# Digite um item: banana
# 
# 1 Adicionar item
# 2 Remover item
# 3 Ver lista
# 4 Sair
# Escolha uma opção: 3
# ['maçã']
# 
# 1 Adicionar item
# 2 Remover item
# 3 Ver lista
# 4 Sair
# Escolha uma opção: 4
# ```

# In[1]:


# solução

""" # 1. Crie uma lista vazia para armazenar os itens da lista de compras.
lista_itens_compras = []

# 2. Crie um loop infinito que imprima um menu de opções ao usuário e permita que ele escolha uma opção.
while True:
    print("\n1 Adicionar item")
    print("2 Remover item")
    print("3 Ver lista")
    print("4 Sair")

    opcao = input("Escolha uma opção: ")

    # 3. Dentro do loop, use uma declaração if para executar a tarefa apropriada de acordo com a escolha do usuário.
    if opcao == '1':
        # 4. Se o usuário escolher adicionar um item, solicite que ele digite o nome do item e adicione-o à lista.
        item_adicionar = input("Digite um item: ")
        lista_itens_compras.append(item_adicionar)
        print()  # Adiciona uma linha em branco para melhor formatação

    elif opcao == '2':
        # 5. Se o usuário escolher remover um item, solicite que ele digite o nome do item e remova-o da lista.
        item_remover = input("Digite um item: ")
        if item_remover in lista_itens_compras:
            lista_itens_compras.remove(item_remover)
        else:
            print("Item não encontrado na lista.")
        print()  # Adiciona uma linha em branco para melhor formatação

    elif opcao == '3':
        # 6. Se o usuário escolher ver a lista, mostre cada item da lista em sua própria linha.
        print(lista_itens_compras)
        print()  # Adiciona uma linha em branco para melhor formatação

    elif opcao == '4':
        # 7. Se o usuário escolher sair, encerre o loop usando break.
        break

    else:
        print("Opção inválida. Por favor, escolha entre 1 e 4.")
        print()  # Adiciona uma linha em branco para melhor formatação """

# ### Segunda versão da lista de compras
# 

# Mude o programa de lista de compras para usar um dicionário ao invés de uma lista.
# O programa deve ter as mesmas funcionalidades, mas agora deve ser possível
# adicionar mais de uma unidade de um item na lista de compras. Ou seja, o dicionário
# deve armazenar o nome do item e a quantidade desejada pelo usuário. Por exemplo,
# se o usuário digitar "banana" e "2", o dicionário deve armazenar "banana" como chave
# e 2 como valor. A estrutura do dicionário ficaria assim: `{"banana": 2}`.
# 
# O programa deve permitir que o usuário adicione, remova e visualize o dicionário de compras.
# 
# Além disso, o programa deve mostrar uma mensagem de erro se o usuário tentar
# usar uma opção inválida do menu. Por exemplo, se o usuário digitar 5, o programa
# deve mostrar a mensagem "Opção inválida. Por favor, escolha uma opção válida." e
# mostrar o menu novamente. Além disso, o programa deve ser *case insensitive*, ou seja,
# "Maçã" e "maçã" devem ser considerados o mesmo item.
# 
# Exemplo de saída:
# 
# ```
# 1 Adicionar item
# 2 Remover item
# 3 Ver lista
# 4 Sair
# Escolha uma opção: 1
# Digite um item: banana
# Digite a quantidade: 2
# 
# 1 Adicionar item
# 2 Remover item
# 3 Ver lista
# 4 Sair
# Escolha uma opção: 1
# Digite um item: maçã
# Digite a quantidade: 3
# 
# 1 Adicionar item
# 2 Remover item
# 3 Ver lista
# 4 Sair
# Escolha uma opção: 3
# {'banana': 2, 'maçã': 3}
# 
# 1 Adicionar item
# 2 Remover item
# 3 Ver lista
# 4 Sair
# Escolha uma opção: 2
# Digite um item: banana
# Digite a quantidade: 1
# 
# 1 Adicionar item
# 2 Remover item
# 3 Ver lista
# 4 Sair
# Escolha uma opção: 3
# {'banana': 1, 'maçã': 3}
# 
# 1 Adicionar item
# 2 Remover item
# 3 Ver lista
# 4 Sair
# Escolha uma opção: 4
# ```
# 

# In[ ]:


# solução

""" # 1. Crie um dicionário vazio para armazenar os itens da lista de compras.
lista_itens_compras = {}

# 2. Crie um loop infinito que imprima um menu de opções ao usuário e permita que ele escolha uma opção.
while True:
    print("\n1 Adicionar item à lista")
    print("2 Remover item da lista") # Menu correto: Opção 2 é Remover item
    print("3 Ver lista de compras")
    print("4 Sair")

    opcao = input("Digite o número da opção desejada: ")

    # 3. Dentro do loop, use uma declaração if para executar a tarefa apropriada de acordo com a escolha do usuário.
    if opcao == '1':
        # 4. Se o usuário escolher adicionar um item, solicite que ele digite o nome do item e adicione-o à lista.
        item_adicionar = input("Digite o item que deseja adicionar: ").strip() # .strip() remove espaços extras no início e fim
        if item_adicionar: # Verifica se o item não está vazio
            quantidade_adicionar = input("Digite a quantidade: ") # Solicita a quantidade do item
            try:
                quantidade_adicionar = int(quantidade_adicionar) # Converte a quantidade para inteiro
                if item_adicionar.lower() in lista_itens_compras: # Verifica se o item (deixando case-insensitive) já está no dicionário
                    lista_itens_compras[item_adicionar.lower()] += quantidade_adicionar # Adiciona a quantidade ao item existente (chave em lowercase)
                else:
                    lista_itens_compras[item_adicionar.lower()] = quantidade_adicionar # Adiciona o novo item com a quantidade (chave em lowercase)
                print(f"'{item_adicionar}' (quantidade: {quantidade_adicionar}) foi adicionado à lista de compras.")
            except ValueError: # Captura erro se a quantidade não for um número inteiro
                print("Quantidade inválida. Por favor, digite um número inteiro.")
        else:
            print("Por favor, digite um nome de item válido.")

    elif opcao == '2':
        # 5. Se o usuário escolher remover um item, solicite que ele digite o nome do item e remova-o da lista. # Comentário CORRIGIDO: Opção 2 é Remover item
        item_remover = input("Digite o item que deseja remover: ").lower() # Converte para lowercase para case-insensitive
        if item_remover in lista_itens_compras: # Verifica se o item (deixando case-insensitive) está no dicionário
            quantidade_remover = input("Digite a quantidade para remover: ") # Solicita a quantidade a ser removida
            try:
                quantidade_remover = int(quantidade_remover) # Converte a quantidade para inteiro
                if quantidade_remover >= lista_itens_compras[item_remover]: # Verifica se a quantidade a remover é maior ou igual à quantidade atual
                    del lista_itens_compras[item_remover] # Remove o item do dicionário
                    print(f"'{item_remover}' removido da lista de compras.")
                else:
                    lista_itens_compras[item_remover] -= quantidade_remover # Diminui a quantidade do item no dicionário
                    print(f"{quantidade_remover} unidade(s) de '{item_remover}' removida(s) da lista de compras.")
            except ValueError: # Captura erro se a quantidade não for um número inteiro
                print("Quantidade inválida. Por favor, digite um número inteiro.")
        else:
            print("Item não encontrado na lista de compras.")

    elif opcao == '3':
        # 6. Se o usuário escolher ver a lista, mostre o dicionário de compras.
        if not lista_itens_compras: # Verifica se a lista está vazia
            print("Sua lista de compras está vazia.")
        else:
            print("Sua lista de compras:")
            for item, quantidade in lista_itens_compras.items(): # Itera sobre os itens e quantidades do dicionário
                print(f"- {item}: {quantidade}") # Imprime o item e a quantidade

    elif opcao == '4':
        # 7. Se o usuário escolher sair, encerre o loop usando break.
        print("Obrigado por usar a lista de compras!")
        break # Sai do loop e encerra o programa

    else:
        # Mensagem de erro para opções inválidas
        print("Opção inválida. Por favor, digite um número de 1 a 4.") """

# ### Terceira versão da lista de compras

# Mantenha o programa da lista de compras com dicionário, mas agora use funções para organizar o código. Crie funções para cada uma das opções do menu: `adicionar_item`, `remover_item` e `ver_lista`. Crie também uma função para mostrar o menu. O programa deve continuar funcionando da mesma forma, mas agora o código deve estar organizado em funções.
# 

# In[ ]:


# solução

""" # 1. Crie um dicionário vazio para armazenar os itens da lista de compras (mantendo a estrutura anterior).
lista_itens_compras = {}

def mostrar_menu():
    """
"""
    Função para exibir o menu de opções para o usuário.
    """
"""
    print("\n1 Adicionar item à lista")
    print("2 Remover item da lista")
    print("3 Ver lista de compras")
    print("4 Sair")

def adicionar_item(lista_compras):
    """
"""
    Função para adicionar um item à lista de compras.
    Solicita o nome e a quantidade do item ao usuário e atualiza o dicionário.
    """
"""
    item_adicionar = input("Digite o item que deseja adicionar: ").strip() # .strip() remove espaços extras no início e fim
    if item_adicionar: # Verifica se o item não está vazio
        quantidade_adicionar = input("Digite a quantidade: ") # Solicita a quantidade do item
        try:
            quantidade_adicionar = int(quantidade_adicionar) # Converte a quantidade para inteiro
            if item_adicionar.lower() in lista_compras: # Verifica se o item (deixando case-insensitive) já está no dicionário
                lista_compras[item_adicionar.lower()] += quantidade_adicionar # Adiciona a quantidade ao item existente (chave em lowercase)
            else:
                lista_compras[item_adicionar.lower()] = quantidade_adicionar # Adiciona o novo item com a quantidade (chave em lowercase)
            print(f"Item '{item_adicionar}' com a quantidade: {quantidade_adicionar} foi adicionado à lista de compras.")
        except ValueError: # Captura erro se a quantidade não for um número inteiro
            print("Quantidade inválida. Por favor, digite um número inteiro.")
    else:
        print("Por favor, digite um nome de item válido.")

def remover_item(lista_compras):
    """
"""
    Função para remover um item da lista de compras.
    Solicita o nome e a quantidade do item a ser removido e atualiza o dicionário.
    """
"""
    item_remover = input("Digite o item que deseja remover: ").lower() # Converte para lowercase para case-insensitive
    if item_remover in lista_compras: # Verifica se o item (deixando case-insensitive) está no dicionário
        quantidade_remover = input("Digite a quantidade para remover: ") # Solicita a quantidade a ser removida
        try:
            quantidade_remover = int(quantidade_remover) # Converte a quantidade para inteiro
            if quantidade_remover >= lista_compras[item_remover]: # Verifica se a quantidade a remover é maior ou igual à quantidade atual
                del lista_compras[item_remover] # Remove o item do dicionário
                print(f"'{item_remover}' removido da lista de compras.")
            else:
                lista_compras[item_remover] -= quantidade_remover # Diminui a quantidade do item no dicionário
                print(f"{quantidade_remover} unidade(s) de '{item_remover}' removida(s) da lista de compras.")
        except ValueError: # Captura erro se a quantidade não for um número inteiro
            print("Quantidade inválida. Por favor, digite um número inteiro.")
    else:
        print("Item não encontrado na lista de compras.")

def ver_lista(lista_compras):
    """
"""
    Função para exibir a lista de compras atual.
    Mostra os itens e suas respectivas quantidades.
    """
"""
    if not lista_compras: # Verifica se a lista está vazia
        print("Sua lista de compras está vazia.")
    else:
        print("Sua lista de compras:")
        for item, quantidade in lista_compras.items(): # Itera sobre os itens e quantidades do dicionário
            print(f"- {item}: {quantidade}") # Imprime o item e a quantidade

# 2. Crie um loop infinito que imprima um menu de opções ao usuário e permita que ele escolha uma opção.
while True:
    mostrar_menu() # Chama a função para exibir o menu
    opcao = input("Digite o número da opção desejada: ")

    # 3. Dentro do loop, use uma declaração if para executar a tarefa apropriada de acordo com a escolha do usuário.
    if opcao == '1':
        # 4. Se o usuário escolher adicionar um item, chama a função adicionar_item.
        adicionar_item(lista_itens_compras) # Chama a função para adicionar item
    elif opcao == '2':
        # 5. Se o usuário escolher remover um item, chama a função remover_item.
        remover_item(lista_itens_compras) # Chama a função para remover item
    elif opcao == '3':
        # 6. Se o usuário escolher ver a lista, chama a função ver_lista.
        ver_lista(lista_itens_compras) # Chama a função para ver a lista
    elif opcao == '4':
        # 7. Se o usuário escolher sair, encerre o loop usando break.
        print("Obrigado por usar a lista de compras!")
        break # Sai do loop e encerra o programa
    else:
        # Mensagem de erro para opções inválidas
        print("Opção inválida. Por favor, digite um número de 1 a 4.") """

# ## Previsão de vendas

# ### Primeira versão da previsão de vendas

# Escreva um programa que preveja as vendas totais para cada produto em uma empresa.
# O usuário deve digitar o nome do produto, as vendas do mês atual e a taxa de crescimento,
# e o programa deve calcular as vendas previstas para o próximo mês.
# 
# Estruture seu programa da seguinte forma:
# 
# 1. Crie um dicionário vazio para armazenar as previsões de vendas.
# 2. Crie um loop infinito que solicite ao usuário o nome do produto, as vendas do mês atual e a taxa de crescimento.
# 3. Dentro do loop, use uma declaração if para verificar se o usuário digitou 'sair'.
# 4. Se o usuário digitar 'sair', encerre o loop usando break.
# 5. Se o usuário digitar qualquer outra coisa, use as entradas para calcular as vendas previstas e adicione-as ao dicionário.
# 6. Depois que o loop for encerrado, use um loop for para iterar sobre o dicionário e mostrar as previsões de vendas para cada produto.
# 
# Exemplo de saída:
# 
# ```
# Digite o nome do produto (ou 'sair' para sair): iphone
# Digite as vendas do mês atual: 10000
# Digite a taxa de crescimento (%): 10
# Digite o nome do produto (ou 'sair' para sair): capinha para iphone
# Digite as vendas do mês atual: 200
# Digite a taxa de crescimento (%): 20
# Digite o nome do produto (ou 'sair' para sair): sair
# iphone: Previsão de vendas do próximo mês = R$ 11000.00
# capinha para iphone: Previsão de vendas do próximo mês = R$ 240.00
# ```
# 

# In[ ]:


# solução

""" # 1. Crie um dicionário vazio para armazenar as previsões de vendas.
previsoes_vendas = {}

# 2. Crie um loop infinito que solicite ao usuário o nome do produto, as vendas do mês atual e a taxa de crescimento.
while True:
    nome_produto = input("Digite o nome do produto (ou 'sair' para sair): ")

    # 3. Dentro do loop, use uma declaração if para verificar se o usuário digitou 'sair'.
    if nome_produto.lower() == 'sair':
        # 4. Se o usuário digitar 'sair', encerre o loop usando break.
        break
    else:
            vendas_atual = float(input("Digite as vendas do mês atual: "))
            taxa_crescimento = float(input("Digite a taxa de crescimento (%): "))

            # 5. Se o usuário digitar qualquer outra coisa, use as entradas para calcular as vendas previstas e adicione-as ao dicionário.
            taxa_crescimento_decimal = taxa_crescimento / 100  # Converter porcentagem para decimal
            vendas_previstas = vendas_atual * (1 + taxa_crescimento_decimal)
            previsoes_vendas[nome_produto] = vendas_previstas

# 6. Depois que o loop for encerrado, use um loop for para iterar sobre o dicionário e mostrar as previsões de vendas para cada produto.
print("\nPrevisões de vendas:")
for produto, previsao in previsoes_vendas.items():
    print(f"{produto}: Previsão de vendas do próximo mês = R$ {previsao:.2f}")

# ### Segunda versão da previsão de vendas """
# 

# Mantenha a mesma funcionalidade do programa anterior, mas agora valide a entrada do usuário.
# Se o usuário digitar um valor inválido para vendas ou taxa de crescimento, mostre a mensagem
# "Entrada inválida. Por favor, digite um número para vendas e taxa de crescimento." e peça
# para o usuário digitar novamente. Tal validação deve ser feita usando try/except.
# 

# In[ ]:


# solução

""" # 1. Crie um dicionário vazio para armazenar as previsões de vendas.
previsoes_vendas = {}

# 2. Crie um loop infinito que solicite ao usuário o nome do produto, as vendas do mês atual e a taxa de crescimento.
while True:
    nome_produto = input("Digite o nome do produto (ou 'sair' para sair): ")

    # 3. Dentro do loop, use uma declaração if para verificar se o usuário digitou 'sair'.
    if nome_produto.lower() == 'sair':
        # 4. Se o usuário digitar 'sair', encerre o loop usando break.
        break
    else:
        try: # Se o usuário digitar um valor inválido para vendas ou taxa de crescimento, mostre a mensagem
            # para o usuário digitar novamente. Tal validação deve ser feita usando try/except.
            vendas_atual = float(input("Digite as vendas do mês atual: "))
            taxa_crescimento = float(input("Digite a taxa de crescimento (%): "))

            # 5. Se o usuário digitar qualquer outra coisa, use as entradas para calcular as vendas previstas e adicione-as ao dicionário.
            taxa_crescimento_decimal = taxa_crescimento / 100  # Converter porcentagem para decimal
            vendas_previstas = vendas_atual * (1 + taxa_crescimento_decimal)
            previsoes_vendas[nome_produto] = vendas_previstas

        except ValueError:
            print("Entrada inválida. Por favor, digite um número para vendas e taxa de crescimento.")

# 6. Depois que o loop for encerrado, use um loop for para iterar sobre o dicionário e mostrar as previsões de vendas para cada produto.
print("\nPrevisões de vendas:")
for produto, previsao in previsoes_vendas.items():
    print(f"{produto}: Previsão de vendas do próximo mês = R$ {previsao:.2f}")
 """

# ## Relatório de vendas

# ### Primeira versão do relatório de vendas

# Escreva um programa que calcula o total e a média de vendas para cada vendedor em uma empresa.
# O usuário deve digitar o nome do vendedor e suas vendas, e o programa deve manter o controle
# do total e da média de vendas para cada vendedor.
# 
# Estruture seu programa da seguinte forma:
# 
# 1. Crie um dicionário vazio para armazenar os dados de vendas.
# 2. Crie um loop infinito que solicite ao usuário o nome do vendedor e suas vendas.
# 3. Dentro do loop, use uma declaração if para verificar se o usuário digitou 'sair'.
# 4. Se o usuário digitar 'sair', encerre o loop usando break.
# 5. Se o usuário digitar qualquer outra coisa, use as entradas para calcular o total e a média de vendas para o vendedor e adicione-os ao dicionário.
# 6. Depois que o loop for encerrado, use um loop for para iterar sobre o dicionário e mostrar o total e a média de vendas para cada vendedor.
# 
# Exemplo de saída:
#     
# ```
# Digite o nome do vendedor (ou 'sair' para sair): João
# Digite as vendas: 100
# Digite o nome do vendedor (ou 'sair' para sair): Maria
# Digite as vendas: 200
# Digite o nome do vendedor (ou 'sair' para sair): João
# Digite as vendas: 300
# Digite o nome do vendedor (ou 'sair' para sair): sair
# João: Total de vendas = R$ 400.0, Média de vendas = R$ 200.0
# Maria: Total de vendas = R$ 200.0, Média de vendas = R$ 200.0
# ```
# 
# Dica: use o método sum() para calcular o total de vendas e o método len() para calcular o número de vendas.
# 

# In[ ]:


# solução

""" # 1. Crie um dicionário vazio para armazenar os dados de vendas.
vendas_vendedores = {}

# 2. Crie um loop infinito que solicite ao usuário o nome do vendedor e suas vendas.
while True:
    nome_vendedor = input("Digite o nome do vendedor (ou 'sair' para sair): ")

    # 3. Dentro do loop, use uma declaração if para verificar se o usuário digitou 'sair'.
    if nome_vendedor.lower() == 'sair':
        # 4. Se o usuário digitar 'sair', encerre o loop usando break.
        break
    else:
            vendas = float(input("Digite as vendas: "))

            # 5. Se o usuário digitar qualquer outra coisa, use as entradas para calcular o total e a média de vendas para o vendedor e adicione-os ao dicionário.
            if nome_vendedor in vendas_vendedores:
                vendas_vendedores[nome_vendedor].append(vendas) # Adiciona a nova venda à lista existente do vendedor
            else:
                vendas_vendedores[nome_vendedor] = [vendas] # Cria uma nova lista com a venda para o novo vendedor

# 6. Depois que o loop for encerrado, use um loop for para iterar sobre o dicionário e mostrar o total e a média de vendas para cada vendedor.
print("\nRelatório de vendas:")
for vendedor, lista_vendas in vendas_vendedores.items():
    total_vendas = sum(lista_vendas) # Usa sum() para calcular o total de vendas
    media_vendas = total_vendas / len(lista_vendas) # Usa len() para calcular a média de vendas
    print(f"{vendedor}: Total de vendas = R$ {total_vendas:.1f}, Média de vendas = R$ {media_vendas:.1f}") """

# ### Segunda versão do relatório de vendas
# 

# Mantenha a mesma funcionalidade do programa anterior, mas agora valide a entrada do usuário.
# Se o usuário digitar um valor inválido para vendas, mostre a mensagem
# "Entrada inválida. Por favor, digite um número para vendas." e peça para o usuário digitar
# novamente. Tal validação deve ser feita usando try/except.
# 
# Além disso, ao invés de armazenar cada venda em uma lista para cada vendedor, armazene
# o total de vendas e a quantidade de vendas em um dicionário. Por exemplo, se o usuário
# digitar "João" e "1000" para vendas, o dicionário deve ficar assim:
# 
# ```python
# {'João': {'total_vendas': 1000, 'quantidade_vendas': 1}}
# ```
# 
# Se, após, o usuário digitar "João" e "2000" para vendas, o dicionário deve ficar assim:
# 
# ```python
# {'João': {'total_vendas': 3000, 'quantidade_vendas': 2}}
# ```
# 
# Perceba como o total de vendas de João aumentou em 2000, assim como a quantidade aumentou em uma unidade.
# 
# Ao final, mostre o total de vendas e a média de vendas de cada vendedor.
# 
# Exemplo de saída:
# 
# ```
# Digite o nome do vendedor (ou 'sair' para sair): João
# Digite as vendas: 1000
# Digite o nome do vendedor (ou 'sair' para sair): Maria
# Digite as vendas: 2000
# Digite o nome do vendedor (ou 'sair' para sair): João
# Digite as vendas: 2000
# Digite o nome do vendedor (ou 'sair' para sair): Maria
# Digite as vendas: 3000
# Digite o nome do vendedor (ou 'sair' para sair): sair
# João: Total de vendas = R$ 3000.00, Média de vendas = R$ 1500.00
# Maria: Total de vendas = R$ 5000.00, Média de vendas = R$ 2500.00
# ```
# 

# In[ ]:


# solução

""" # 1. Crie um dicionário vazio para armazenar os dados de vendas.
vendas_vendedores = {}

# 2. Crie um loop infinito que solicite ao usuário o nome do vendedor e suas vendas.
while True:
    nome_vendedor = input("Digite o nome do vendedor (ou 'sair' para sair): ")

    # 3. Dentro do loop, use uma declaração if para verificar se o usuário digitou 'sair'.
    if nome_vendedor.lower() == 'sair':
        # 4. Se o usuário digitar 'sair', encerre o loop usando break.
        break
    else:
        while True: # Loop para validar a entrada de vendas
            vendas_str = input("Digite as vendas: ")
            try:
                vendas = float(vendas_str)
                # 5. Se o usuário digitar qualquer outra coisa, use as entradas para calcular o total e a média de vendas para o vendedor e adicione-os ao dicionário.
                if nome_vendedor in vendas_vendedores:
                    # Atualiza o total de vendas e a quantidade se o vendedor já existe
                    vendas_vendedores[nome_vendedor]['total_vendas'] += vendas
                    vendas_vendedores[nome_vendedor]['quantidade_vendas'] += 1
                else:
                    # Cria uma nova entrada para o vendedor com o total de vendas e quantidade iniciais
                    vendas_vendedores[nome_vendedor] = {'total_vendas': vendas, 'quantidade_vendas': 1}
                break # Sai do loop de validação se a entrada for válida
            except ValueError:
                # Validação de entrada: Se o usuário digitar um valor inválido para vendas
                print("Entrada inválida. Por favor, digite um número para vendas.") # Mensagem de erro para entrada inválida

# 6. Depois que o loop for encerrado, use um loop for para iterar sobre o dicionário e mostrar o total e a média de vendas para cada vendedor.
print("\nRelatório de vendas:")
for vendedor, dados_vendas in vendas_vendedores.items():
    total_vendas = dados_vendas['total_vendas'] # Obtém o total de vendas do dicionário interno
    quantidade_vendas = dados_vendas['quantidade_vendas'] # Obtém a quantidade de vendas do dicionário interno
    media_vendas = total_vendas / quantidade_vendas if quantidade_vendas > 0 else 0 # Calcula a média, evitando divisão por zero
    print(f"{vendedor}: Total de vendas = R$ {total_vendas:.2f}, Média de vendas = R$ {media_vendas:.2f}")
 """
# ### Terceira versão do relatório de vendas

#  Mantenha a funcionalidade do programa, mas agora use funções para organizar o código. Crie funções para cada uma das operações:
#  `solicitar_nome_vendedor`, `solicitar_vendas` , `atualizar_dados` e `print_dados`. O programa deve continuar funcionando da mesma forma, mas agora o código deve estar organizado em funções.

# In[ ]:


# solução

# # 1. Crie um dicionário vazio para armazenar os dados de vendas.
# vendas_vendedores = {}

# def solicitar_nome_vendedor():
#     """
#     Função para solicitar e retornar o nome do vendedor ao usuário.
#     """
#     return input("Digite o nome do vendedor (ou 'sair' para sair): ")

# def solicitar_vendas():
#     """
#     Função para solicitar e validar a entrada de vendas do usuário.
#     Retorna o valor de vendas como float se a entrada for válida, senão retorna None.
#     """
#     while True: # Loop para garantir que o usuário digite um valor de vendas válido
#         vendas_str = input("Digite as vendas: ")
#         try:
#             vendas = float(vendas_str)
#             return vendas # Retorna o valor de vendas se for válido
#         except ValueError:
#             # Validação de entrada: Se o usuário digitar um valor inválido para vendas
#             print("Entrada inválida. Por favor, digite um número para vendas.") # Mensagem de erro para entrada inválida

# def atualizar_dados(dados_vendas, nome, vendas):
#     """
#     Função para atualizar o dicionário de dados de vendas com as vendas de um vendedor.
#     Atualiza o total de vendas e a quantidade de vendas para o vendedor especificado.
#     """
#     if nome in dados_vendas:
#         # Atualiza o total de vendas e a quantidade se o vendedor já existe
#         dados_vendas[nome]['total_vendas'] += vendas
#         dados_vendas[nome]['quantidade_vendas'] += 1
#     else:
#         # Cria uma nova entrada para o vendedor com o total de vendas e quantidade iniciais
#         dados_vendas[nome] = {'total_vendas': vendas, 'quantidade_vendas': 1}

# def print_dados(dados_vendas):
#     """
#     Função para imprimir o relatório de vendas final.
#     Itera sobre o dicionário de dados de vendas e exibe o total e a média de vendas para cada vendedor.
#     """
#     print("\nRelatório de vendas:")
#     for vendedor, dados_vendedor in dados_vendas.items():
#         total_vendas = dados_vendedor['total_vendas'] # Obtém o total de vendas do dicionário interno
#         quantidade_vendas = dados_vendedor['quantidade_vendas'] # Obtém a quantidade de vendas do dicionário interno
#         media_vendas = total_vendas / quantidade_vendas if quantidade_vendas > 0 else 0 # Calcula a média, evitando divisão por zero
#         print(f"{vendedor}: Total de vendas = R$ {total_vendas:.2f}, Média de vendas = R$ {media_vendas:.2f}")

# # 2. Crie um loop infinito que solicite ao usuário o nome do vendedor e suas vendas.
# while True:
#     # Usa a função para solicitar o nome do vendedor
#     nome_vendedor = solicitar_nome_vendedor()

#     # 3. Dentro do loop, use uma declaração if para verificar se o usuário digitou 'sair'.
#     if nome_vendedor.lower() == 'sair':
#         # 4. Se o usuário digitar 'sair', encerre o loop usando break.
#         break
#     else:
#         # Usa a função para solicitar as vendas e já valida a entrada
#         vendas = solicitar_vendas()
#         if vendas is not None: # Verifica se vendas é um valor válido (não None)
#             # 5. Se o usuário digitar qualquer outra coisa, use as entradas para calcular o total e a média de vendas para o vendedor e adicione-os ao dicionário.
#             atualizar_dados(vendas_vendedores, nome_vendedor, vendas) # Usa a função para atualizar os dados de vendas

# # 6. Depois que o loop for encerrado, use um loop for para iterar sobre o dicionário e mostrar o total e a média de vendas para cada vendedor.
# print_dados(vendas_vendedores) # Usa a função para imprimir o relatório de vendas

# ## Analisador de texto

# Crie um programa que analise um texto fornecido pelo usuário.
# O programa deve contar o número de palavras (independentemente se há repetição ou não),
# a quantidade de cada palavra e a
# quantidade de cada letra. Ignore maiúsculas e minúsculas ao contar letras.
# Não se preocupe com pontuação e espaços ao contar palavras.
# 
# O programa deve conter uma função chamada `analisar_texto` que recebe o texto
# como parâmetro e retorna a contagem de palavras, a frequência de palavras e a
# frequência de letras.
# 
# Para o texto "Olá mundo! Este é um teste. Olá novamente." o programa deve
# imprimir:
#     
# ```
# Contagem de palavras: 8
# Frequência de palavras: {'Olá': 2, 'mundo!': 1, 'Este': 1, 'é': 1, 'um': 1, 'teste.': 1, 'novamente.': 1}
# Frequência de letras: {'o': 4, 'l': 2, 'á': 2, 'm': 3, 'u': 2, 'n': 3, 'd': 1, '!': 1, 'e': 6, 's': 2, 't': 4, 'é': 1, '.': 2, 'v': 1, 'a': 1}
# ```
# 
# **Observação**: Mais adiante no curso, aprenderemos a lidar com a pontuação.

# In[ ]:


# solução

#!/usr/bin/env python
# coding: utf-8

# # Exercícios de fixação 

# A seguir, você encontrará alguns exercícios para fixar os conceitos aprendidos no curso até agora. Os exercícios estão divididos por exemplos práticos da vida real:
# 
# - lista de compras
# - previsão de vendas
# - relatório de vendas
# - segmentação de clientes
# - analisador de texto
# 
# Para cada assunto, você encontrará ao menos um exercício. Nos casos onde há mais de um exercício para o mesmo assunto, você será convidado a resolver o mesmo problema de formas diferentes. Isso é proposital, pois o objetivo é que você pratique o que aprendeu e, ao mesmo tempo, aprenda novas formas de resolver um mesmo problema. Por exemplo, usando diferentes estruturas de dados, ou diferentes formas de iterar sobre uma estrutura de dados, ou, ainda, utilizando funções.
# 
# Tente resolver os exercícios sozinho. Se tiver dificuldades, consulte o material do curso e, se ainda assim não conseguir resolver, consulte a solução.

# ## Lista de compras

# ### Primeira versão da lista de compras

# Escreva um programa que permita que um usuário crie uma lista de compras.
# O usuário deve ser capaz de adicionar itens, remover itens e visualizar a lista.
# 
# Estruture seu programa da seguinte forma:
# 
# 1. Crie uma lista vazia para armazenar os itens da lista de compras.
# 2. Crie um loop infinito que imprima um menu de opções ao usuário e permita que ele escolha uma opção.
# 3. Dentro do loop, use uma declaração if para executar a tarefa apropriada de acordo com a escolha do usuário.
# 4. Se o usuário escolher adicionar um item, solicite que ele digite o nome do item e adicione-o à lista.
# 5. Se o usuário escolher remover um item, solicite que ele digite o nome do item e remova-o da lista.
# 6. Se o usuário escolher ver a lista, mostre cada item da lista em sua própria linha.
# 7. Se o usuário escolher sair, encerre o loop usando break.
# 
# Exemplo de saída:
# 
# ```
# 1 Adicionar item
# 2 Remover item
# 3 Ver lista
# 4 Sair
# Escolha uma opção: 1
# Digite um item: banana
# 
# 1 Adicionar item
# 2 Remover item
# 3 Ver lista
# 4 Sair
# Escolha uma opção: 1
# Digite um item: maçã
# 
# 1 Adicionar item
# 2 Remover item
# 3 Ver lista
# 4 Sair
# Escolha uma opção: 3
# ['banana', 'maçã']
# 
# 1 Adicionar item
# 2 Remover item
# 3 Ver lista
# 4 Sair
# Escolha uma opção: 2
# Digite um item: banana
# 
# 1 Adicionar item
# 2 Remover item
# 3 Ver lista
# 4 Sair
# Escolha uma opção: 3
# ['maçã']
# 
# 1 Adicionar item
# 2 Remover item
# 3 Ver lista
# 4 Sair
# Escolha uma opção: 4
# ```

# In[1]:


# solução

""" # 1. Crie uma lista vazia para armazenar os itens da lista de compras.
lista_itens_compras = []

# 2. Crie um loop infinito que imprima um menu de opções ao usuário e permita que ele escolha uma opção.
while True:
    print("\n1 Adicionar item")
    print("2 Remover item")
    print("3 Ver lista")
    print("4 Sair")

    opcao = input("Escolha uma opção: ")

    # 3. Dentro do loop, use uma declaração if para executar a tarefa apropriada de acordo com a escolha do usuário.
    if opcao == '1':
        # 4. Se o usuário escolher adicionar um item, solicite que ele digite o nome do item e adicione-o à lista.
        item_adicionar = input("Digite um item: ")
        lista_itens_compras.append(item_adicionar)
        print()  # Adiciona uma linha em branco para melhor formatação

    elif opcao == '2':
        # 5. Se o usuário escolher remover um item, solicite que ele digite o nome do item e remova-o da lista.
        item_remover = input("Digite um item: ")
        if item_remover in lista_itens_compras:
            lista_itens_compras.remove(item_remover)
        else:
            print("Item não encontrado na lista.")
        print()  # Adiciona uma linha em branco para melhor formatação

    elif opcao == '3':
        # 6. Se o usuário escolher ver a lista, mostre cada item da lista em sua própria linha.
        print(lista_itens_compras)
        print()  # Adiciona uma linha em branco para melhor formatação

    elif opcao == '4':
        # 7. Se o usuário escolher sair, encerre o loop usando break.
        break

    else:
        print("Opção inválida. Por favor, escolha entre 1 e 4.")
        print()  # Adiciona uma linha em branco para melhor formatação """

# ### Segunda versão da lista de compras
# 

# Mude o programa de lista de compras para usar um dicionário ao invés de uma lista.
# O programa deve ter as mesmas funcionalidades, mas agora deve ser possível
# adicionar mais de uma unidade de um item na lista de compras. Ou seja, o dicionário
# deve armazenar o nome do item e a quantidade desejada pelo usuário. Por exemplo,
# se o usuário digitar "banana" e "2", o dicionário deve armazenar "banana" como chave
# e 2 como valor. A estrutura do dicionário ficaria assim: `{"banana": 2}`.
# 
# O programa deve permitir que o usuário adicione, remova e visualize o dicionário de compras.
# 
# Além disso, o programa deve mostrar uma mensagem de erro se o usuário tentar
# usar uma opção inválida do menu. Por exemplo, se o usuário digitar 5, o programa
# deve mostrar a mensagem "Opção inválida. Por favor, escolha uma opção válida." e
# mostrar o menu novamente. Além disso, o programa deve ser *case insensitive*, ou seja,
# "Maçã" e "maçã" devem ser considerados o mesmo item.
# 
# Exemplo de saída:
# 
# ```
# 1 Adicionar item
# 2 Remover item
# 3 Ver lista
# 4 Sair
# Escolha uma opção: 1
# Digite um item: banana
# Digite a quantidade: 2
# 
# 1 Adicionar item
# 2 Remover item
# 3 Ver lista
# 4 Sair
# Escolha uma opção: 1
# Digite um item: maçã
# Digite a quantidade: 3
# 
# 1 Adicionar item
# 2 Remover item
# 3 Ver lista
# 4 Sair
# Escolha uma opção: 3
# {'banana': 2, 'maçã': 3}
# 
# 1 Adicionar item
# 2 Remover item
# 3 Ver lista
# 4 Sair
# Escolha uma opção: 2
# Digite um item: banana
# Digite a quantidade: 1
# 
# 1 Adicionar item
# 2 Remover item
# 3 Ver lista
# 4 Sair
# Escolha uma opção: 3
# {'banana': 1, 'maçã': 3}
# 
# 1 Adicionar item
# 2 Remover item
# 3 Ver lista
# 4 Sair
# Escolha uma opção: 4
# ```
# 

# In[ ]:


# solução

""" # 1. Crie um dicionário vazio para armazenar os itens da lista de compras.
lista_itens_compras = {}

# 2. Crie um loop infinito que imprima um menu de opções ao usuário e permita que ele escolha uma opção.
while True:
    print("\n1 Adicionar item à lista")
    print("2 Remover item da lista") # Menu correto: Opção 2 é Remover item
    print("3 Ver lista de compras")
    print("4 Sair")

    opcao = input("Digite o número da opção desejada: ")

    # 3. Dentro do loop, use uma declaração if para executar a tarefa apropriada de acordo com a escolha do usuário.
    if opcao == '1':
        # 4. Se o usuário escolher adicionar um item, solicite que ele digite o nome do item e adicione-o à lista.
        item_adicionar = input("Digite o item que deseja adicionar: ").strip() # .strip() remove espaços extras no início e fim
        if item_adicionar: # Verifica se o item não está vazio
            quantidade_adicionar = input("Digite a quantidade: ") # Solicita a quantidade do item
            try:
                quantidade_adicionar = int(quantidade_adicionar) # Converte a quantidade para inteiro
                if item_adicionar.lower() in lista_itens_compras: # Verifica se o item (deixando case-insensitive) já está no dicionário
                    lista_itens_compras[item_adicionar.lower()] += quantidade_adicionar # Adiciona a quantidade ao item existente (chave em lowercase)
                else:
                    lista_itens_compras[item_adicionar.lower()] = quantidade_adicionar # Adiciona o novo item com a quantidade (chave em lowercase)
                print(f"'{item_adicionar}' (quantidade: {quantidade_adicionar}) foi adicionado à lista de compras.")
            except ValueError: # Captura erro se a quantidade não for um número inteiro
                print("Quantidade inválida. Por favor, digite um número inteiro.")
        else:
            print("Por favor, digite um nome de item válido.")

    elif opcao == '2':
        # 5. Se o usuário escolher remover um item, solicite que ele digite o nome do item e remova-o da lista. # Comentário CORRIGIDO: Opção 2 é Remover item
        item_remover = input("Digite o item que deseja remover: ").lower() # Converte para lowercase para case-insensitive
        if item_remover in lista_itens_compras: # Verifica se o item (deixando case-insensitive) está no dicionário
            quantidade_remover = input("Digite a quantidade para remover: ") # Solicita a quantidade a ser removida
            try:
                quantidade_remover = int(quantidade_remover) # Converte a quantidade para inteiro
                if quantidade_remover >= lista_itens_compras[item_remover]: # Verifica se a quantidade a remover é maior ou igual à quantidade atual
                    del lista_itens_compras[item_remover] # Remove o item do dicionário
                    print(f"'{item_remover}' removido da lista de compras.")
                else:
                    lista_itens_compras[item_remover] -= quantidade_remover # Diminui a quantidade do item no dicionário
                    print(f"{quantidade_remover} unidade(s) de '{item_remover}' removida(s) da lista de compras.")
            except ValueError: # Captura erro se a quantidade não for um número inteiro
                print("Quantidade inválida. Por favor, digite um número inteiro.")
        else:
            print("Item não encontrado na lista de compras.")

    elif opcao == '3':
        # 6. Se o usuário escolher ver a lista, mostre o dicionário de compras.
        if not lista_itens_compras: # Verifica se a lista está vazia
            print("Sua lista de compras está vazia.")
        else:
            print("Sua lista de compras:")
            for item, quantidade in lista_itens_compras.items(): # Itera sobre os itens e quantidades do dicionário
                print(f"- {item}: {quantidade}") # Imprime o item e a quantidade

    elif opcao == '4':
        # 7. Se o usuário escolher sair, encerre o loop usando break.
        print("Obrigado por usar a lista de compras!")
        break # Sai do loop e encerra o programa

    else:
        # Mensagem de erro para opções inválidas
        print("Opção inválida. Por favor, digite um número de 1 a 4.") """

# ### Terceira versão da lista de compras

# Mantenha o programa da lista de compras com dicionário, mas agora use funções para organizar o código. Crie funções para cada uma das opções do menu: `adicionar_item`, `remover_item` e `ver_lista`. Crie também uma função para mostrar o menu. O programa deve continuar funcionando da mesma forma, mas agora o código deve estar organizado em funções.
# 

# In[ ]:


# solução

""" # 1. Crie um dicionário vazio para armazenar os itens da lista de compras (mantendo a estrutura anterior).
lista_itens_compras = {}

def mostrar_menu():
    """
"""
    Função para exibir o menu de opções para o usuário.
    """
"""
    print("\n1 Adicionar item à lista")
    print("2 Remover item da lista")
    print("3 Ver lista de compras")
    print("4 Sair")

def adicionar_item(lista_compras):
    """
"""
    Função para adicionar um item à lista de compras.
    Solicita o nome e a quantidade do item ao usuário e atualiza o dicionário.
    """
"""
    item_adicionar = input("Digite o item que deseja adicionar: ").strip() # .strip() remove espaços extras no início e fim
    if item_adicionar: # Verifica se o item não está vazio
        quantidade_adicionar = input("Digite a quantidade: ") # Solicita a quantidade do item
        try:
            quantidade_adicionar = int(quantidade_adicionar) # Converte a quantidade para inteiro
            if item_adicionar.lower() in lista_compras: # Verifica se o item (deixando case-insensitive) já está no dicionário
                lista_compras[item_adicionar.lower()] += quantidade_adicionar # Adiciona a quantidade ao item existente (chave em lowercase)
            else:
                lista_compras[item_adicionar.lower()] = quantidade_adicionar # Adiciona o novo item com a quantidade (chave em lowercase)
            print(f"Item '{item_adicionar}' com a quantidade: {quantidade_adicionar} foi adicionado à lista de compras.")
        except ValueError: # Captura erro se a quantidade não for um número inteiro
            print("Quantidade inválida. Por favor, digite um número inteiro.")
    else:
        print("Por favor, digite um nome de item válido.")

def remover_item(lista_compras):
    """
"""
    Função para remover um item da lista de compras.
    Solicita o nome e a quantidade do item a ser removido e atualiza o dicionário.
    """
"""
    item_remover = input("Digite o item que deseja remover: ").lower() # Converte para lowercase para case-insensitive
    if item_remover in lista_compras: # Verifica se o item (deixando case-insensitive) está no dicionário
        quantidade_remover = input("Digite a quantidade para remover: ") # Solicita a quantidade a ser removida
        try:
            quantidade_remover = int(quantidade_remover) # Converte a quantidade para inteiro
            if quantidade_remover >= lista_compras[item_remover]: # Verifica se a quantidade a remover é maior ou igual à quantidade atual
                del lista_compras[item_remover] # Remove o item do dicionário
                print(f"'{item_remover}' removido da lista de compras.")
            else:
                lista_compras[item_remover] -= quantidade_remover # Diminui a quantidade do item no dicionário
                print(f"{quantidade_remover} unidade(s) de '{item_remover}' removida(s) da lista de compras.")
        except ValueError: # Captura erro se a quantidade não for um número inteiro
            print("Quantidade inválida. Por favor, digite um número inteiro.")
    else:
        print("Item não encontrado na lista de compras.")

def ver_lista(lista_compras):
    """
"""
    Função para exibir a lista de compras atual.
    Mostra os itens e suas respectivas quantidades.
    """
"""
    if not lista_compras: # Verifica se a lista está vazia
        print("Sua lista de compras está vazia.")
    else:
        print("Sua lista de compras:")
        for item, quantidade in lista_compras.items(): # Itera sobre os itens e quantidades do dicionário
            print(f"- {item}: {quantidade}") # Imprime o item e a quantidade

# 2. Crie um loop infinito que imprima um menu de opções ao usuário e permita que ele escolha uma opção.
while True:
    mostrar_menu() # Chama a função para exibir o menu
    opcao = input("Digite o número da opção desejada: ")

    # 3. Dentro do loop, use uma declaração if para executar a tarefa apropriada de acordo com a escolha do usuário.
    if opcao == '1':
        # 4. Se o usuário escolher adicionar um item, chama a função adicionar_item.
        adicionar_item(lista_itens_compras) # Chama a função para adicionar item
    elif opcao == '2':
        # 5. Se o usuário escolher remover um item, chama a função remover_item.
        remover_item(lista_itens_compras) # Chama a função para remover item
    elif opcao == '3':
        # 6. Se o usuário escolher ver a lista, chama a função ver_lista.
        ver_lista(lista_itens_compras) # Chama a função para ver a lista
    elif opcao == '4':
        # 7. Se o usuário escolher sair, encerre o loop usando break.
        print("Obrigado por usar a lista de compras!")
        break # Sai do loop e encerra o programa
    else:
        # Mensagem de erro para opções inválidas
        print("Opção inválida. Por favor, digite um número de 1 a 4.") """

# ## Previsão de vendas

# ### Primeira versão da previsão de vendas

# Escreva um programa que preveja as vendas totais para cada produto em uma empresa.
# O usuário deve digitar o nome do produto, as vendas do mês atual e a taxa de crescimento,
# e o programa deve calcular as vendas previstas para o próximo mês.
# 
# Estruture seu programa da seguinte forma:
# 
# 1. Crie um dicionário vazio para armazenar as previsões de vendas.
# 2. Crie um loop infinito que solicite ao usuário o nome do produto, as vendas do mês atual e a taxa de crescimento.
# 3. Dentro do loop, use uma declaração if para verificar se o usuário digitou 'sair'.
# 4. Se o usuário digitar 'sair', encerre o loop usando break.
# 5. Se o usuário digitar qualquer outra coisa, use as entradas para calcular as vendas previstas e adicione-as ao dicionário.
# 6. Depois que o loop for encerrado, use um loop for para iterar sobre o dicionário e mostrar as previsões de vendas para cada produto.
# 
# Exemplo de saída:
# 
# ```
# Digite o nome do produto (ou 'sair' para sair): iphone
# Digite as vendas do mês atual: 10000
# Digite a taxa de crescimento (%): 10
# Digite o nome do produto (ou 'sair' para sair): capinha para iphone
# Digite as vendas do mês atual: 200
# Digite a taxa de crescimento (%): 20
# Digite o nome do produto (ou 'sair' para sair): sair
# iphone: Previsão de vendas do próximo mês = R$ 11000.00
# capinha para iphone: Previsão de vendas do próximo mês = R$ 240.00
# ```
# 

# In[ ]:


# solução

""" # 1. Crie um dicionário vazio para armazenar as previsões de vendas.
previsoes_vendas = {}

# 2. Crie um loop infinito que solicite ao usuário o nome do produto, as vendas do mês atual e a taxa de crescimento.
while True:
    nome_produto = input("Digite o nome do produto (ou 'sair' para sair): ")

    # 3. Dentro do loop, use uma declaração if para verificar se o usuário digitou 'sair'.
    if nome_produto.lower() == 'sair':
        # 4. Se o usuário digitar 'sair', encerre o loop usando break.
        break
    else:
            vendas_atual = float(input("Digite as vendas do mês atual: "))
            taxa_crescimento = float(input("Digite a taxa de crescimento (%): "))

            # 5. Se o usuário digitar qualquer outra coisa, use as entradas para calcular as vendas previstas e adicione-as ao dicionário.
            taxa_crescimento_decimal = taxa_crescimento / 100  # Converter porcentagem para decimal
            vendas_previstas = vendas_atual * (1 + taxa_crescimento_decimal)
            previsoes_vendas[nome_produto] = vendas_previstas

# 6. Depois que o loop for encerrado, use um loop for para iterar sobre o dicionário e mostrar as previsões de vendas para cada produto.
print("\nPrevisões de vendas:")
for produto, previsao in previsoes_vendas.items():
    print(f"{produto}: Previsão de vendas do próximo mês = R$ {previsao:.2f}")

# ### Segunda versão da previsão de vendas """
# 

# Mantenha a mesma funcionalidade do programa anterior, mas agora valide a entrada do usuário.
# Se o usuário digitar um valor inválido para vendas ou taxa de crescimento, mostre a mensagem
# "Entrada inválida. Por favor, digite um número para vendas e taxa de crescimento." e peça
# para o usuário digitar novamente. Tal validação deve ser feita usando try/except.
# 

# In[ ]:


# solução

""" # 1. Crie um dicionário vazio para armazenar as previsões de vendas.
previsoes_vendas = {}

# 2. Crie um loop infinito que solicite ao usuário o nome do produto, as vendas do mês atual e a taxa de crescimento.
while True:
    nome_produto = input("Digite o nome do produto (ou 'sair' para sair): ")

    # 3. Dentro do loop, use uma declaração if para verificar se o usuário digitou 'sair'.
    if nome_produto.lower() == 'sair':
        # 4. Se o usuário digitar 'sair', encerre o loop usando break.
        break
    else:
        try: # Se o usuário digitar um valor inválido para vendas ou taxa de crescimento, mostre a mensagem
            # para o usuário digitar novamente. Tal validação deve ser feita usando try/except.
            vendas_atual = float(input("Digite as vendas do mês atual: "))
            taxa_crescimento = float(input("Digite a taxa de crescimento (%): "))

            # 5. Se o usuário digitar qualquer outra coisa, use as entradas para calcular as vendas previstas e adicione-as ao dicionário.
            taxa_crescimento_decimal = taxa_crescimento / 100  # Converter porcentagem para decimal
            vendas_previstas = vendas_atual * (1 + taxa_crescimento_decimal)
            previsoes_vendas[nome_produto] = vendas_previstas

        except ValueError:
            print("Entrada inválida. Por favor, digite um número para vendas e taxa de crescimento.")

# 6. Depois que o loop for encerrado, use um loop for para iterar sobre o dicionário e mostrar as previsões de vendas para cada produto.
print("\nPrevisões de vendas:")
for produto, previsao in previsoes_vendas.items():
    print(f"{produto}: Previsão de vendas do próximo mês = R$ {previsao:.2f}")
 """

# ## Relatório de vendas

# ### Primeira versão do relatório de vendas

# Escreva um programa que calcula o total e a média de vendas para cada vendedor em uma empresa.
# O usuário deve digitar o nome do vendedor e suas vendas, e o programa deve manter o controle
# do total e da média de vendas para cada vendedor.
# 
# Estruture seu programa da seguinte forma:
# 
# 1. Crie um dicionário vazio para armazenar os dados de vendas.
# 2. Crie um loop infinito que solicite ao usuário o nome do vendedor e suas vendas.
# 3. Dentro do loop, use uma declaração if para verificar se o usuário digitou 'sair'.
# 4. Se o usuário digitar 'sair', encerre o loop usando break.
# 5. Se o usuário digitar qualquer outra coisa, use as entradas para calcular o total e a média de vendas para o vendedor e adicione-os ao dicionário.
# 6. Depois que o loop for encerrado, use um loop for para iterar sobre o dicionário e mostrar o total e a média de vendas para cada vendedor.
# 
# Exemplo de saída:
#     
# ```
# Digite o nome do vendedor (ou 'sair' para sair): João
# Digite as vendas: 100
# Digite o nome do vendedor (ou 'sair' para sair): Maria
# Digite as vendas: 200
# Digite o nome do vendedor (ou 'sair' para sair): João
# Digite as vendas: 300
# Digite o nome do vendedor (ou 'sair' para sair): sair
# João: Total de vendas = R$ 400.0, Média de vendas = R$ 200.0
# Maria: Total de vendas = R$ 200.0, Média de vendas = R$ 200.0
# ```
# 
# Dica: use o método sum() para calcular o total de vendas e o método len() para calcular o número de vendas.
# 

# In[ ]:


# solução

""" # 1. Crie um dicionário vazio para armazenar os dados de vendas.
vendas_vendedores = {}

# 2. Crie um loop infinito que solicite ao usuário o nome do vendedor e suas vendas.
while True:
    nome_vendedor = input("Digite o nome do vendedor (ou 'sair' para sair): ")

    # 3. Dentro do loop, use uma declaração if para verificar se o usuário digitou 'sair'.
    if nome_vendedor.lower() == 'sair':
        # 4. Se o usuário digitar 'sair', encerre o loop usando break.
        break
    else:
            vendas = float(input("Digite as vendas: "))

            # 5. Se o usuário digitar qualquer outra coisa, use as entradas para calcular o total e a média de vendas para o vendedor e adicione-os ao dicionário.
            if nome_vendedor in vendas_vendedores:
                vendas_vendedores[nome_vendedor].append(vendas) # Adiciona a nova venda à lista existente do vendedor
            else:
                vendas_vendedores[nome_vendedor] = [vendas] # Cria uma nova lista com a venda para o novo vendedor

# 6. Depois que o loop for encerrado, use um loop for para iterar sobre o dicionário e mostrar o total e a média de vendas para cada vendedor.
print("\nRelatório de vendas:")
for vendedor, lista_vendas in vendas_vendedores.items():
    total_vendas = sum(lista_vendas) # Usa sum() para calcular o total de vendas
    media_vendas = total_vendas / len(lista_vendas) # Usa len() para calcular a média de vendas
    print(f"{vendedor}: Total de vendas = R$ {total_vendas:.1f}, Média de vendas = R$ {media_vendas:.1f}") """

# ### Segunda versão do relatório de vendas
# 

# Mantenha a mesma funcionalidade do programa anterior, mas agora valide a entrada do usuário.
# Se o usuário digitar um valor inválido para vendas, mostre a mensagem
# "Entrada inválida. Por favor, digite um número para vendas." e peça para o usuário digitar
# novamente. Tal validação deve ser feita usando try/except.
# 
# Além disso, ao invés de armazenar cada venda em uma lista para cada vendedor, armazene
# o total de vendas e a quantidade de vendas em um dicionário. Por exemplo, se o usuário
# digitar "João" e "1000" para vendas, o dicionário deve ficar assim:
# 
# ```python
# {'João': {'total_vendas': 1000, 'quantidade_vendas': 1}}
# ```
# 
# Se, após, o usuário digitar "João" e "2000" para vendas, o dicionário deve ficar assim:
# 
# ```python
# {'João': {'total_vendas': 3000, 'quantidade_vendas': 2}}
# ```
# 
# Perceba como o total de vendas de João aumentou em 2000, assim como a quantidade aumentou em uma unidade.
# 
# Ao final, mostre o total de vendas e a média de vendas de cada vendedor.
# 
# Exemplo de saída:
# 
# ```
# Digite o nome do vendedor (ou 'sair' para sair): João
# Digite as vendas: 1000
# Digite o nome do vendedor (ou 'sair' para sair): Maria
# Digite as vendas: 2000
# Digite o nome do vendedor (ou 'sair' para sair): João
# Digite as vendas: 2000
# Digite o nome do vendedor (ou 'sair' para sair): Maria
# Digite as vendas: 3000
# Digite o nome do vendedor (ou 'sair' para sair): sair
# João: Total de vendas = R$ 3000.00, Média de vendas = R$ 1500.00
# Maria: Total de vendas = R$ 5000.00, Média de vendas = R$ 2500.00
# ```
# 

# In[ ]:


# solução

""" # 1. Crie um dicionário vazio para armazenar os dados de vendas.
vendas_vendedores = {}

# 2. Crie um loop infinito que solicite ao usuário o nome do vendedor e suas vendas.
while True:
    nome_vendedor = input("Digite o nome do vendedor (ou 'sair' para sair): ")

    # 3. Dentro do loop, use uma declaração if para verificar se o usuário digitou 'sair'.
    if nome_vendedor.lower() == 'sair':
        # 4. Se o usuário digitar 'sair', encerre o loop usando break.
        break
    else:
        while True: # Loop para validar a entrada de vendas
            vendas_str = input("Digite as vendas: ")
            try:
                vendas = float(vendas_str)
                # 5. Se o usuário digitar qualquer outra coisa, use as entradas para calcular o total e a média de vendas para o vendedor e adicione-os ao dicionário.
                if nome_vendedor in vendas_vendedores:
                    # Atualiza o total de vendas e a quantidade se o vendedor já existe
                    vendas_vendedores[nome_vendedor]['total_vendas'] += vendas
                    vendas_vendedores[nome_vendedor]['quantidade_vendas'] += 1
                else:
                    # Cria uma nova entrada para o vendedor com o total de vendas e quantidade iniciais
                    vendas_vendedores[nome_vendedor] = {'total_vendas': vendas, 'quantidade_vendas': 1}
                break # Sai do loop de validação se a entrada for válida
            except ValueError:
                # Validação de entrada: Se o usuário digitar um valor inválido para vendas
                print("Entrada inválida. Por favor, digite um número para vendas.") # Mensagem de erro para entrada inválida

# 6. Depois que o loop for encerrado, use um loop for para iterar sobre o dicionário e mostrar o total e a média de vendas para cada vendedor.
print("\nRelatório de vendas:")
for vendedor, dados_vendas in vendas_vendedores.items():
    total_vendas = dados_vendas['total_vendas'] # Obtém o total de vendas do dicionário interno
    quantidade_vendas = dados_vendas['quantidade_vendas'] # Obtém a quantidade de vendas do dicionário interno
    media_vendas = total_vendas / quantidade_vendas if quantidade_vendas > 0 else 0 # Calcula a média, evitando divisão por zero
    print(f"{vendedor}: Total de vendas = R$ {total_vendas:.2f}, Média de vendas = R$ {media_vendas:.2f}")
 """
# ### Terceira versão do relatório de vendas

#  Mantenha a funcionalidade do programa, mas agora use funções para organizar o código. Crie funções para cada uma das operações:
#  `solicitar_nome_vendedor`, `solicitar_vendas` , `atualizar_dados` e `print_dados`. O programa deve continuar funcionando da mesma forma, mas agora o código deve estar organizado em funções.

# In[ ]:


# solução

# # 1. Crie um dicionário vazio para armazenar os dados de vendas.
# vendas_vendedores = {}

# def solicitar_nome_vendedor():
#     """
#     Função para solicitar e retornar o nome do vendedor ao usuário.
#     """
#     return input("Digite o nome do vendedor (ou 'sair' para sair): ")

# def solicitar_vendas():
#     """
#     Função para solicitar e validar a entrada de vendas do usuário.
#     Retorna o valor de vendas como float se a entrada for válida, senão retorna None.
#     """
#     while True: # Loop para garantir que o usuário digite um valor de vendas válido
#         vendas_str = input("Digite as vendas: ")
#         try:
#             vendas = float(vendas_str)
#             return vendas # Retorna o valor de vendas se for válido
#         except ValueError:
#             # Validação de entrada: Se o usuário digitar um valor inválido para vendas
#             print("Entrada inválida. Por favor, digite um número para vendas.") # Mensagem de erro para entrada inválida

# def atualizar_dados(dados_vendas, nome, vendas):
#     """
#     Função para atualizar o dicionário de dados de vendas com as vendas de um vendedor.
#     Atualiza o total de vendas e a quantidade de vendas para o vendedor especificado.
#     """
#     if nome in dados_vendas:
#         # Atualiza o total de vendas e a quantidade se o vendedor já existe
#         dados_vendas[nome]['total_vendas'] += vendas
#         dados_vendas[nome]['quantidade_vendas'] += 1
#     else:
#         # Cria uma nova entrada para o vendedor com o total de vendas e quantidade iniciais
#         dados_vendas[nome] = {'total_vendas': vendas, 'quantidade_vendas': 1}

# def print_dados(dados_vendas):
#     """
#     Função para imprimir o relatório de vendas final.
#     Itera sobre o dicionário de dados de vendas e exibe o total e a média de vendas para cada vendedor.
#     """
#     print("\nRelatório de vendas:")
#     for vendedor, dados_vendedor in dados_vendas.items():
#         total_vendas = dados_vendedor['total_vendas'] # Obtém o total de vendas do dicionário interno
#         quantidade_vendas = dados_vendedor['quantidade_vendas'] # Obtém a quantidade de vendas do dicionário interno
#         media_vendas = total_vendas / quantidade_vendas if quantidade_vendas > 0 else 0 # Calcula a média, evitando divisão por zero
#         print(f"{vendedor}: Total de vendas = R$ {total_vendas:.2f}, Média de vendas = R$ {media_vendas:.2f}")

# # 2. Crie um loop infinito que solicite ao usuário o nome do vendedor e suas vendas.
# while True:
#     # Usa a função para solicitar o nome do vendedor
#     nome_vendedor = solicitar_nome_vendedor()

#     # 3. Dentro do loop, use uma declaração if para verificar se o usuário digitou 'sair'.
#     if nome_vendedor.lower() == 'sair':
#         # 4. Se o usuário digitar 'sair', encerre o loop usando break.
#         break
#     else:
#         # Usa a função para solicitar as vendas e já valida a entrada
#         vendas = solicitar_vendas()
#         if vendas is not None: # Verifica se vendas é um valor válido (não None)
#             # 5. Se o usuário digitar qualquer outra coisa, use as entradas para calcular o total e a média de vendas para o vendedor e adicione-os ao dicionário.
#             atualizar_dados(vendas_vendedores, nome_vendedor, vendas) # Usa a função para atualizar os dados de vendas

# # 6. Depois que o loop for encerrado, use um loop for para iterar sobre o dicionário e mostrar o total e a média de vendas para cada vendedor.
# print_dados(vendas_vendedores) # Usa a função para imprimir o relatório de vendas


# ## Segmentação de clientes

# ### Primeira versão da segmentação de clientes

# Escreva um programa que segmenta clientes com base em suas compras totais.
# O usuário deve digitar o nome do cliente e suas compras totais, e o programa
# deve atribuir cada cliente a um segmento: 'Bronze' para compras de até R\\$ 1000,
# 'Prata' para compras de até R\\$ 5000 e 'Ouro' para compras acima de R\\$ 5000.
# 
# Estruture seu programa da seguinte forma:
# 
# 1. Crie um dicionário vazio para armazenar os clientes e seus segmentos.
# 2. Crie um loop infinito que solicite ao usuário o nome do cliente e suas compras totais.
# 3. Dentro do loop, use uma declaração if para atribuir o segmento apropriado ao cliente.
# 4. Se o usuário digitar 'sair' para o nome do cliente, encerre o loop usando break.
# 5. Fora do loop, use um loop for para imprimir o nome e o segmento de cada cliente.
# 
# Exemplo de saída:
#     
# ```
# Digite o nome do cliente (ou 'sair' para sair): João
# Digite o total de compras: 100
# Digite o nome do cliente (ou 'sair' para sair): Maria
# Digite o total de compras: 2000
# Digite o nome do cliente (ou 'sair' para sair): José
# Digite o total de compras: 6000
# Digite o nome do cliente (ou 'sair' para sair): sair
# João: Segmento do Cliente = Bronze
# Maria: Segmento do Cliente = Prata
# José: Segmento do Cliente = Ouro
# ```
# 

# In[ ]:


# solução

# 1. Crie um dicionário vazio para armazenar os clientes e seus segmentos.
clientes = {}

# 2. Crie um loop infinito que solicite ao usuário o nome do cliente e suas compras totais.
while True:
    nome_cliente = input("Digite o nome do cliente (ou 'sair' para sair): ")
    
# 4. Se o usuário digitar 'sair' para o nome do cliente, encerre o loop usando break.
    if nome_cliente.lower() == "sair":
         break
    
# 3. Dentro do loop, use uma declaração if para atribuir o segmento apropriado ao cliente.    
    vendas = int(input("Digite o total de compras: "))

    if vendas <= 1000:
        segmento = "Bronze"
        
    if vendas > 1000 and vendas <= 5000:
        segmento = "Prata"
        
    if vendas > 5000:
        segmento = "Ouro"
    clientes[nome_cliente] = segmento
            
# 5. Fora do loop, use um loop for para imprimir o nome e o segmento de cada cliente.
for nome_cliente, segmento in clientes.items():
    print(f"{nome_cliente} Segmento do Cliente = {segmento}")

# ### Segunda versão da segmentação de clientes
# 

# 
# Mantenha a mesma funcionalidade do programa anterior, mas agora valide a entrada do usuário.
# Se o usuário digitar um valor inválido para compras, mostre a mensagem
# "Entrada inválida. Por favor, digite um número para compras." e peça para o usuário digitar
# novamente. Tal validação deve ser feita usando try/except.
# 
# Além disso, ao invés de deixar os limites de compras fixos no programa, armazene-os em uma
# lista de tuplas. Por exemplo:
# 
# ```python
# segmentos = [(1000, 'Bronze'), (5000, 'Prata'), (float('inf'), 'Ouro')]
# ``` 
# 
# Assim, outros segmentos podem ser adicionados facilmente. O primeiro elemento da tupla é o
# limite de compras e o segundo é o nome do segmento. O último elemento da lista é uma tupla
# com limite `float('inf')`, que representa o segmento Ouro. Isso significa que, se o valor de
# compras for maior que todos os limites, o segmento será Ouro.
# 
# Depois, percorra essa lista e, para cada tupla, verifique se o valor de compras é menor ou igual
# ao limite. Se for, armazene o segmento em um dicionário. Por exemplo, se o usuário digitar
# "João" e "500" para compras, o dicionário deve ficar assim:
# `{'João': 'Bronze'}`
# 

# In[ ]:


# solução
 


# ### Terceira versão da segmentação de clientes

# Mantenha a funcionalidade do programa, mas agora use funções para organizar o código. Crie funções para cada uma das operações: `solicitar_nome_cliente`, `solicitar_total_compras` e `atribuir_segmento` e `print_segmento_por_cliente`. O programa deve continuar funcionando da mesma forma, mas agora o código deve estar organizado em funções. Além disso, normalize que todos os nomes sejam armazenados em letras minúsculas.

# In[ ]:


# solução


# ## Analisador de texto

# Crie um programa que analise um texto fornecido pelo usuário.
# O programa deve contar o número de palavras (independentemente se há repetição ou não),
# a quantidade de cada palavra e a
# quantidade de cada letra. Ignore maiúsculas e minúsculas ao contar letras.
# Não se preocupe com pontuação e espaços ao contar palavras.
# 
# O programa deve conter uma função chamada `analisar_texto` que recebe o texto
# como parâmetro e retorna a contagem de palavras, a frequência de palavras e a
# frequência de letras.
# 
# Para o texto "Olá mundo! Este é um teste. Olá novamente." o programa deve
# imprimir:
#     
# ```
# Contagem de palavras: 8
# Frequência de palavras: {'Olá': 2, 'mundo!': 1, 'Este': 1, 'é': 1, 'um': 1, 'teste.': 1, 'novamente.': 1}
# Frequência de letras: {'o': 4, 'l': 2, 'á': 2, 'm': 3, 'u': 2, 'n': 3, 'd': 1, '!': 1, 'e': 6, 's': 2, 't': 4, 'é': 1, '.': 2, 'v': 1, 'a': 1}
# ```
# 
# **Observação**: Mais adiante no curso, aprenderemos a lidar com a pontuação.

# In[ ]:


# solução

