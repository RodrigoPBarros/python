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
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
soma = n1 + n2
print("=======DESAFIO 003=======")
print(f"A soma entre {cores['azul_claro']}{n1}{cores['limpa']} e {cores['azul_claro']}{n2}{cores['limpa']} é igual a {cores['verde']}{soma}{cores['limpa']}.")