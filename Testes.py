produtos = ['tv', 'celular', 'tablet', 'mouse', 'teclado', 'geladeira', 'forno', 'xbox']

estoque = [100, 150, 100, 120, 70, 180, 80, 0]

x = 0

while x < 1:

    search = input('Deseja pesquisar a qtd de estoque de algum produto? s/n ')
    if search == 'n':
        print('\033[32mFIM')
        x += 1
    elif search == 's':
        busca = input('Digite o produto que deseja pesquisar: ')
        busca = busca.lower()
        if busca in produtos:
            i = produtos.index(busca)
            print("""
            Produto pesquisado: \033[34m{}\033[m
            Quantidade em estoque: {}
            """.format(produtos[i].upper(), estoque[i]))
            qtdCheck = estoque[i]
            if qtdCheck < 1:
                qtdZero = input('Estoque de {} zerado, gostaria de atualizar a quantidade? s/n '.format(busca.upper()))
                if qtdZero == 's':
                    qtdAtualiza = int(input('Insira a quantidade atualizada'))
                    estoque[i] = qtdAtualiza
                    print("""
                    Estoque de \033[32m{}\033[m atualizado
                    Quantidade atual: {}
                    """.format(busca, qtdAtualiza))
                else:
                    print('ok')
        else:
            print('\033[31m{}\033[m não cadastrado'.format(busca.upper()))
            nc = input('Gostaria de cadastrar {} no estoque? s/n: '.format(busca))
            if nc == 's':
                w = 0
                while w < 1:
                    produtos.append(busca.lower())
                    qtd = int(input('Qual a quantidade em estoque? '))
                    if qtd:
                        estoque.append(qtd)
                        print('\033[32m{}\033[m cadastrado com sucesso'.format(busca.upper()))
                        w += 1
                    else:
                        print('Digite a quantidade corretamente"APENAS NUMEROS"')
            elif nc == 'n':
                print('Ok')
    else:
        print('\033[31mDigite apenas s ou n\033[m')