def boas_vindas():
    print('olá')
    print('Temos 5 notbooks em estoque')

boas_vindas()

def somar_doisnumeros():            # variáveis com o mesmo nome  em funções diferentes podem se chamadas, pois são tratadas independentemente
    numero1 = 5
    numero2 = 5
    resultado = numero1 +numero2
    print(resultado)

def somar_doisnumeros1():                                               
    numero1 = 5
    numero2 = 9
    resultado = numero1 +numero2
    print(resultado)

somar_doisnumeros()
somar_doisnumeros1()
