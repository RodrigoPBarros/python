import math
from math import radians, sin, cos, tan

angulo = float(input('Digite o valor do ângulo: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print("=======DESAFIO 018=======")
print(f"O seno do ângulo é {seno:.2f}.")
print(f"O cosseno do ângulo é {cosseno:.2f}.")
print(f"A tangente do ângulo é {tangente:.2f}.")