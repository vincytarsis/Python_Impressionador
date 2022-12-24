produtos = ['tv', 'celular', 'tablet', 'mouse', 'teclado', 'geladeira', 'forno', 'xbox'] # Lista com o nome dos produtos
estoque = [100, 150, 100, 120, 70, 180, 80, 0] # Lista com a quantidade de produtos
x = 0

while x < 1:
    search = input('Deseja pesquisar a quantidade de estoque de algum produto? S/N: ').lower() # Ação do usuario
    if search == 'n':
        print('\033[32mFIM')
        x += 1
    elif search == 's':
        busca = input('Digite o produto que deseja pesquisar: ').lower() # Deixa o nome do produto minusculo

        if busca in produtos: # Faz uma busca na lista de produtos
            i = produtos.index(busca)
            print(f'Produto pesquisado: \033[34m{produtos[i]}\033[m Quantidade em estoque: {estoque[i]}')
            # Mostra na tela o produto e valor em estoque

            qtd_check = estoque[i] # Checa a quantidade em estoque, se for 0 pode atualizar ou não para outro valor
            if qtd_check < 1:
                qtd_zero = input(f'Estoque de {busca.upper()} zerado, gostaria de atualizar a quantidade? S/N: ')

                if qtd_zero == 's':
                    qtd_atualiza = int(input('Insira a quantidade atualizada: '))
                    estoque = qtd_atualiza
                    print(f'Estoque de \033[m{busca}\033[m atulizado!\nQuantidade atual: {qtd_atualiza}')
                else:
                    print('Ok')
        # Caso o produto pesquisado não esteja no estoque, tem a opção de adicionalo
        else:
            print(f'\033[31m{busca.upper()}\033[m não cadastrado!')
            nc = input(f'Gostaria de cadastrar {busca} no estoque? S/N: ')
            if nc == 's':
                w = 0
                while w < 1:
                    produtos.append(busca.lower())
                    qtd = int(input('Qual a quantidade em estoque? '))
                    if qtd:
                        estoque.append(qtd)
                        print(f'\033[32m{busca.upper()}\033[m cadastrado com sucesso!')
                        w += 1
                    else:
                        print('Digite a quantidade corretamente "APENAS NUMEROS"')

            elif nc == 'n':
                print('ok')
    else:
        print('\033[31mDigite apenas S ou N\033[m')
