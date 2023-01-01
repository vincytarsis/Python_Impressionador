def padronizar_codigos(lista_codigos, padrao='m'):
    for i in range(len(lista_codigos)):
        lista_codigos[i] = lista_codigos[i].strip()
        if padrao == 'm':
            lista_codigos[i] = lista_codigos[i].lower()
        else:
            lista_codigos[i] = lista_codigos[i].upper()
    return lista_codigos

cod_produtos = ['  ABC12  ', 'abc34', 'AbC37']
print(padronizar_codigos(cod_produtos, padrao='M'))