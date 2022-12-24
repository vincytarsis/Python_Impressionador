print('='*7, 'HOTEL TRÊS PONTAS', '='*7)
print(''*7, 'Seja bem vindo ao nosso hotel...', ''*7)
print('='*6, 'SISTEMA DE CADASTRO', '='*6)

# Quantidade de pessoas que vão estar no quarto
qtd_hospedes = int(input('Quantidade de hóspedes: '))
quarto =[] # Lista vazia

# Loop em hospedes, que vai ser executado a quantos hóspedes tiver
for hospedes in range(qtd_hospedes):
    print(f'     HÓSPEDE {hospedes + 1}') # Mostra qual hóspede deve inserir os dados
    nome = input('NOME: ') # Recebe nome
    cpf = input('CPF: ') # Recebe cpf
    hospede = [nome, cpf] # Guarda nome e cpf na lista hospede
    quarto.append(hospede) # Lista quarto recebe os dados da lista hospede
print('\n', '='*8, 'DADOS DO QUARTO', '='*8)
for i in quarto:
    indice = quarto.index(i)
    print(f'NOME: {quarto[indice][0]}, CPF: {quarto[indice][1]}')