pedido = []

while True:
    produto = str(input('Produto:'))
    pedido.append(produto)
    resp = str(input('Deseja continuar? [S/N] ')).upper().strip()

    while resp not in 'SN':
        resp = str(input('Opção inválida, deseja continuar? [S/N]: ')).upper().strip()

    if resp == 'N':
        break

print(f'Compra finalizada com sucesso. Segue seus produtos: {pedido} ')

