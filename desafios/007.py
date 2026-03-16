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
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2
print("=======DESAFIO 007=======")
print(f"A média entre {cores['azul_claro']}{nota1}{cores['limpa']} e {cores['azul_claro']}{nota2}{cores['limpa']} é {cores['verde']}{media:.1f}{cores['limpa']}.")