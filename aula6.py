valor = int(input("digite o valor do produto"))
while valor > 20:
    valor = (valor * 0.10) + valor
    print(F' O valor final  do seu produto será de R$ {valor}')
    break

#Publicar um produto com comissão de 10% para produtos acima de 20$