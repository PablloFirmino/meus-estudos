#operador ternario
#abaixo seria a forma comum de resolver esse problema envolvendo eleição

#idade = int(input("insira sua idade"))
#if idade >= 16 :
   # print("Você está apto a votar")
#else:
   # print("Você é menor de idade, não está apto a votar")

idade = 10


resultado = "Você está apto a votar" if idade >= 16 else "Você é menor de idade, não está apto a votar"
print(resultado)
#poderia usar o input também como feito acima