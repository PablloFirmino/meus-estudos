#enviar um email com detalhes de uma compra online(maximo 3 tentativas) para compras confirmadas
compra_confirmada = True
dados_compra = "compra no valor de xxx  e entrega confirmada"

for enviar in range (3):
    if compra_confirmada:
     print(dados_compra )
     print('dados enviados para o seu email')
    break                     # sem o break ele roda 3 vezes, e exibe  3 vezes o print, assim o break faz ele rodar 3 vezes,porém 1 print
else:
   print('Falha realizada')