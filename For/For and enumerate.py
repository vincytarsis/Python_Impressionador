produtos = ['apple tv', 'mac', 'iphone x', 'ipad', 'apple watch', 'mac book', 'airpods']
vendas = [1200, 700, 8000, 458, 7000, 10000, 900]
meta = 5000

for i, vendas in enumerate(vendas):
    if vendas < meta:
        print(f'{produtos[i].title()} vendeu {vendas} unidades. Atingindo {vendas/meta:.0%} da meta')
    else:
        print(f'\n{produtos[i].title()} vendeu {vendas} unidades. Atingiu {vendas/meta:.0%} da meta')