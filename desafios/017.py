import math
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

cateto_oposto = float(input('Digite o valor do cateto oposto: '))
cateto_adjacente = float(input('Digite o valor do cateto adjacente: '))
hipotenusa = math.hypot(cateto_oposto, cateto_adjacente)

print("=======DESAFIO 017=======")
print(f"A hipotenusa do triângulo retângulo é {cores['azul_claro']}{hipotenusa:.2f}{cores['limpa']}.")