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
nome = input('Digite seu nome completo: ').strip()
print("=======DESAFIO 027=======")

print(f"Seu nome completo é {cores['verde']}{nome}{cores['limpa']}.")
print(f"Seu primeiro nome é {cores['verde']}{nome.split()[0]}{cores['limpa']}.")
print(f"Seu último nome é {cores['verde']}{nome.split()[-1]}{cores['limpa']}.")