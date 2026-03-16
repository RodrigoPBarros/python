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
numeroreal = float(input("Digite um número real: "))
inteiro = int(numeroreal)

print("=======DESAFIO 016=======")

print(f"A parte inteira do número {cores['azul_claro']}{numeroreal}{cores['limpa']} é {cores['verde']}{inteiro}{cores['limpa']}.")