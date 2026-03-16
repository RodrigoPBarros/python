cores = {"limpa": "\033[m", "verde": "\033[32m", "vermelho": "\033[31m", "azul": "\033[34m", "azul_claro": "\033[36m", "amarelo": "\033[33m", "roxo": "\033[35m", "branco": "\033[37m"}
nome = input('Digite seu nome completo: ').strip()
print("=======DESAFIO 001=======")
print(f"Olá {cores['azul_claro']}{nome}{cores['limpa']}, seja bem-vindo(a)!")