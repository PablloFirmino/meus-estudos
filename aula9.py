def soma(*numeros):
    resultado  = 0
    for num in numeros:
        resultado  += num                           # o * recebe vários números
    return resultado




x = soma(2,3,4,7)

print(x)