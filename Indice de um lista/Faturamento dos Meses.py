meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun','jul', 'ago', 'set', 'out', 'nov', 'dez']
vendas_1sem = [25000, 29000, 22200, 17750, 15870, 19900]
vendas_2sem = [19850, 20120, 17540, 15555, 49051, 9650]

total_vendas = []
total_vendas.extend(vendas_1sem + vendas_2sem)

maior_valor = max(total_vendas)
menor_valor = min(total_vendas)

i_maior_valor = total_vendas.index(maior_valor)
i_menor_valor = total_vendas.index(menor_valor)

faturamento = sum(total_vendas)

percentual = maior_valor / faturamento

print(f'O melhor mês do ano foi {meses[i_maior_valor]}, com {maior_valor}')
print(f'O pior mês do ano foi {meses[i_menor_valor]}, com {menor_valor}')
print(f'Faturamento Total: R${faturamento:,}')
print(f'O melhor mês representou {percentual:.1%} das vendas do ano todo')

