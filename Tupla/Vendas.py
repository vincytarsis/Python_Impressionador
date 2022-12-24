vendas_produtos = [('iphone', 558147, 951642), ('galaxy', 712350, 244295), ('ipad', 573823, 26964), ('tv', 405252, 787604),
                   ('máquina de café', 718654, 867660), ('kildle', 531580, 973139), ('mac book', 892292, 646016),
                   ('notebook dell', 422760, 694913), ('notebook hp', 154753, 539704), ('notebook asus', 887061, 324831),
                   ('microsoft surface', 438508, 667179), ('webcam', 237467, 295633), ('caixa de som', 489705, 725316),
                   ('microfone', 328311, 644622), ('camera canon', 591120, 994303)]

# Para determinar a posição do print (>direita, <esquerda, ^centro)
# Desenhando a tabela

print('{:^20}|{:^20}|{:^20}|{:^20}'.format('PRODUTOS', 'VENDAS2021', 'VENDAS2022', 'CRESCIMENTO ANUAL'))
print('=' * 80)

for item in vendas_produtos:
    produto, vendas2021, vendas2022 = item
    perc = (vendas2022 / vendas2021) - 1

    # Formatando para moedas
    vendas2021 = f'R$ {vendas2021:2,.2f}'
    vendas2022 = f'R$ {vendas2022:2,.2f}'

    # Formatando para porcentagem
    perc1 = (f'{perc:.2%}')

    # Verificando se o percentual é negativo, caso seja printa em vermelho
    if perc > 0:
        print(f'{produto:^20}|{vendas2021:^20}|{vendas2022:^20}|{perc1:^20}')
    else:
        print(f'{produto:^20}|' + f'{vendas2021:^20}|' + f'{vendas2022:^20}|' + f'\033[31m{perc1:^20} \033[m')