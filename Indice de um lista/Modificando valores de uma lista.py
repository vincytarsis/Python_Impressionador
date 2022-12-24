produtos = ['computador', 'livro', 'tablet', 'celular', 'tv', 'ar condicionado', 'alexa', 'máquina de café', 'kindle']

# Cada item da lista dos produtos corresponde a quantidade de vendas no mês e preço, nessa ordem
produtos_ecommerce = [
    [10000, 2500],
    [50000, 40],
    [7000, 1200],
    [20000, 1500],
    [5800, 1300],
    [7200, 2500],
    [200, 800],
    [3300, 700],
    [1900, 400]
]
# Verifica se existe Livro na lista de produtos
if 'livro' in produtos:
    i_livro = produtos.index('livro')

    # Valor total de vendas, antigo
    total_antigo = produtos_ecommerce[i_livro][0] * produtos_ecommerce[i_livro][1]
    # Soma o valor do livro + 10% de imposto
    produtos_ecommerce[i_livro][1] *= 1.1
    # Multiplica o valor do livro pelo total de livros vendidos
    novo_total = produtos_ecommerce[i_livro][0] * produtos_ecommerce[i_livro][1]
    print(f'Vamos pagar de imposto a mais: R${novo_total - total_antigo:,}')

# Caso não haja livro
else:
    print("O prduto livro não se encontra na lista de produtos")