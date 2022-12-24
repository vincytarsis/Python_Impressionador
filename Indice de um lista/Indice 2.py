# Lista de produtos atuais
produtos = ['apple tv', 'mac', 'iphone x', 'ipad', 'apple watch', 'mac book', 'airpods' ]
vendas = [1000, 1500, 15000, 270, 900, 100, 1200]


def linhas():
    print('-' * 80)

print(f'Temos {len(produtos)} produtos a venda')
linhas()
print(produtos)
linhas()

mais = max(vendas)
i = vendas.index(mais)
produto_mais_vendido = produtos[i]
menos = min(vendas)
i = vendas.index(menos)
produto_menos_vendido = produtos[i]

t = len(vendas)
i = list(range(0, len(produtos)))

for a in range(t-1):
    for b in range(a+1, t):
        if vendas[i[a]] < vendas[i[b]]:
            c = i[a]
            i[a] = i[b]
            i[b] = c

while True:

    # Qual ação tomar
    linhas()
    print(f'MENU DE OPÇÕES')
    motivo = input('--------------\n|Excluir\n'
                   '|Trocar\n'
                   '|Mais vendido\n'
                   '|Menos vendido\n'
                   '|Ordem de vendas\n'
                   '|Sair\n --------------'
                   '\n').lower()
    motivo = motivo.casefold()

    # Condição excluir
    if motivo == 'excluir':
        produto = input('Dgite o produto que deseja EXCLUIR da lista: ').lower()

        # Tratamento de erro
        try:
            produtos.remove(produto)
            print(f'O item \033[31m{produto.upper()}\033[m foi excluido corretamente!')
            print(produtos)
        except:
            print(f'\033[31m{produto}\033[m não pertence a lista')

    # Condição trocar
    elif motivo == 'trocar':
        produto = input('Digite o produto que deseja TROCAR da lista: ').lower()

        # Tratamento de erro
        try:
            i = produtos.index(produto)
            item_removido = produtos.pop(i)
            produto = input('Qual o produto que deseja ACRESCENTAR a lista: ').lower()
            produtos[i] = produto
            print(f'Você removeu o item \033[31m{item_removido}\033[m e trocou por \033[32m{produto}\033[m')
            print(produtos)
        except:
            print(f'\033[31m{produto}\033[m não pertence a lista')

    elif motivo == 'mais vendido':
        print(f'O produto mais vendido foi {produto_mais_vendido}, com {mais} vendas')

    elif motivo == 'menos vendido':
        print(f'O produto menos vendido foi {produto_menos_vendido}, com {menos}')

    elif motivo == 'ordem de vendas':
        for a in range(t):
            print(f'Produto {produtos[i[a]]}, vendas {vendas[i[a]]}')

    elif motivo == 'sair':
        break
    else:
        print('\033[33mDigite uma das 5 opções:\033[m')