cpf = input('Digite o seu CPF:')
cpf = cpf.replace('.', '')
cpf = cpf.replace('-', '').strip()
if cpf.isnumeric() and len(cpf) == 11:
    print(cpf)
else:
    print('CPF invalido: Digite os 11 números')
