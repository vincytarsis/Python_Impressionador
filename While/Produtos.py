vendas = []

while True:
    produto = input('Informe o produto:')
    if produto == '':
        break
    else:
        qtde = input('Informe a quantidade que deseja levar: ')
        vendas.append([produto, qtde])

print('-' * 25)
print('{:^12}|{:^12}'.format('Produto', 'Qtde'))
print('-' * 25)

for lista in vendas:
    produto, qtde = lista
    print(f'{produto:<12}|{qtde:>12}')
