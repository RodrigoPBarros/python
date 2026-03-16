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
numero = int(input("Digite um número inteiro: "))
dobro = numero * 2
triplo = numero * 3
raiz_quadrada = numero ** 0.5

print("=======DESAFIO 006=======")

print(f"O dobro de {cores['azul_claro']}{numero}{cores['limpa']} é {cores['verde']}{dobro}{cores['limpa']}.")
print(f"O triplo de {cores['azul_claro']}{numero}{cores['limpa']} é {cores['verde']}{triplo}{cores['limpa']}.")
print(f"A raiz quadrada de {cores['azul_claro']}{numero}{cores['limpa']} é {cores['verde']}{raiz_quadrada:.2f}{cores['limpa']}.")