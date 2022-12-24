meta = 10000
vendas = [
    ['João', 15000],
    ['Julia', 27000],
    ['Marcus', 9900],
    ['Maria', 3750],
    ['Ana', 10300],
    ['Alon', 7870],
]

for nome, valor in vendas:
    if valor >= 10000:
        print(f'O Vendedor {nome} vendeu R$ {valor} e bateu a meta')
    else:
        print(f'O Vendedor {nome} vendeu R$ {valor} e não bateu a meta')