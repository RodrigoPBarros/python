import math

cateto_oposto = float(input('Digite o valor do cateto oposto: '))
cateto_adjacente = float(input('Digite o valor do cateto adjacente: '))
hipotenusa = math.hypot(cateto_oposto, cateto_adjacente)

print("=======DESAFIO 017=======")
print(f"A hipotenusa do triângulo retângulo é {hipotenusa:.2f}.")