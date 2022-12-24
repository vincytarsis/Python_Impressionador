# Produtos e suas contidades vendidas
produtos = [
    'iphone', 'galaxy', 'ipad', 'tv', 'máquina de café', 'kindle', 'geladeira',
    'adega', 'notebook dell', 'notebook hp', 'notebook asus', 'microsof surface',
    'webcam', 'caixa de som', 'microfone', 'camera canon'
]

vendas2021 = [
    558147, 712350, 573823, 405252, 718654, 531580, 973139, 892292, 422760, 154753,
    887061, 438508, 237467, 489705, 328311, 591120
]
vendas2022 = [
    951642, 244295, 26964, 787604, 867660, 78830, 710331, 646016, 694913, 539704, 324831,
    667179, 295633, 725316, 644622, 994303
]

# Formatação da tabela
print('-'*96)
print('|{:^20}  |  {:^20}  |  {:^20}  |  {:^20}|'.format('PRODUTOS', 'VENDAS 2021', 'VENDAS 2022', 'CRESCIMENTO'))
print('-'*96)

# Logica das comparações
for i, produto in enumerate(produtos):
    if vendas2022[i] > vendas2021[i]:
        resultado = (vendas2022[i] / vendas2021[i] - 1) * 100
        print(f'| {produtos[i]:^19}  |  {vendas2021[i]:^19}   |  {vendas2022[i]:^20}  |  {resultado:>+12.2f}%       |')

for i, produto in enumerate(produtos):
    if vendas2022[i] <= vendas2021[i]:
        resultado = (vendas2022[i] / vendas2021[i] - 1) * 100
        print(f'| {produtos[i]:^19}  |  {vendas2021[i]:^19}   |  {vendas2022[i]:^20}  |  {resultado:>+12.2f}%       |')

anual = (sum(vendas2022) / sum(vendas2021) - 1) * 100
print('-'*96)
print('| {:^44}  |  {:^44}  |'.format('TOTAL:', 'CRESCIMENTO DA EMPRESA'))
print('| {:>6} R$ {:<10} | {:>8} R$ {:<10} |  {:>+25.2f}%                    |'.format('2021:', sum(vendas2021), '2022', sum(vendas2022), anual))
print('-'*96)

