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
numero = int(input("Digite um número: "))
antecessor = numero - 1
sucessor = numero + 1
print("=======DESAFIO 005=======")
print(f"O antecessor de {cores['azul_claro']}{numero}{cores['limpa']} é {cores['azul_claro']}{antecessor}{cores['limpa']}.")
print(f"O sucessor de {cores['azul_claro']}{numero}{cores['limpa']} é {cores['azul_claro']}{sucessor}{cores['limpa']}.")  