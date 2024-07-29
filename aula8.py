def cliente1 (nome):
    print( f'olá {nome}')

cliente1('maria')

def cliente2 (nome):
    return f'olá {nome}'

cliente1('josé')                #o Return ele ARMAZENA O VALOR, já o print só exibe na tela
                                # por isso quando rodar, o cliente 1 não vai funcionar, pois não foi usado print

cliente2('maria')

x = cliente1 ('josé')
y = cliente2 ('maria')

print(x)
print(y)