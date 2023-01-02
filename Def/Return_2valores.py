meta = 10000
vendas = {
    'João': 15000,
    'Julia': 27000,
    'Marcus': 9900,
    'Maria': 3750,
    'Ana': 10300,
    'Alon': 7870,
}

def calculo_meta(meta, vendas):
    bateram_meta = []
    for vendedor in vendas:
        if vendas[vendedor] >= meta:
            bateram_meta.append(vendedor)
    perc_bateram_meta = len(bateram_meta) / len(vendas)
    return perc_bateram_meta, bateram_meta

p_meta, vendedores_acima_meta = calculo_meta(meta, vendas)
print(f'{p_meta:.1%}')
print(vendedores_acima_meta)