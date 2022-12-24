nome = input('Digite seu nome:')
email = input('Digite seu e-mail:')

if nome and email:
    pos_a = email.find('@')
    servidor = email[pos_a:]
    if pos_a != -1 and '.' in servidor:
        print('Cadastro Concluido')
    else:
        print('Email inválido')
else:
    print('Digite seu nome e e-mail corretamente')
