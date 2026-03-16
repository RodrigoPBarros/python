import math
from math import radians, sin, cos, tan

cores = {
    "limpa": "\033[m",
    "verde": "\033[32m",
    "vermelho": "\033[31m",
    "azul": "\033[34m",
    "azul_claro": "\033[36m",
    "amarelo": "\033[33m",
    "roxo": "\033[35m",
    "branco": "\033[37m"
}
angulo = float(input('Digite o valor do ângulo: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print("=======DESAFIO 018=======")
print(f"O seno do ângulo é {cores['azul_claro']}{seno:.2f}{cores['limpa']}.")
print(f"O cosseno do ângulo é {cores['vermelho']}{cosseno:.2f}{cores['limpa']}.")
print(f"A tangente do ângulo é {cores['verde']}{tangente:.2f}{cores['limpa']}.")