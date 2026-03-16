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

algo = input("Digite algo: ")
print("=======DESAFIO 004=======")

print(f"O tipo primitivo desse valor é {cores['azul_claro']}{type(algo).__name__}{cores['limpa']}.")
print(f"É alfanumérico? {cores['azul_claro']}{algo.isalnum()}{cores['limpa']}")
print(f"É alfabético? {cores['azul_claro']}{algo.isalpha()}{cores['limpa']}")    
print(f"É um número? {cores['azul_claro']}{algo.isnumeric()}{cores['limpa']}")
print(f"É um espaço? {cores['azul_claro']}{algo.isspace()}{cores['limpa']}")
print(f"Está em maiúsculas? {cores['azul_claro']}{algo.isupper()}{cores['limpa']}")
print(f"Está em minúsculas? {cores['azul_claro']}{algo.islower()}{cores['limpa']}")
print(f"Está capitalizada? {cores['azul_claro']}{algo.istitle()}{cores['limpa']}")
print(f"É um dígito? {cores['azul_claro']}{algo.isdigit()}{cores['limpa']}")
