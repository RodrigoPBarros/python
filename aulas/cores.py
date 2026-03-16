a = 3
b = 5
nome = "Rodrigo"
cores = {"limpa": "\033[m", "verde": "\033[32m", "vermelho": "\033[31m", "azul": "\033[34m", "azul_claro": "\033[36m", "amarelo": "\033[33m", "roxo": "\033[35m", "branco": "\033[37m"}

print(f"Os valores são {cores['verde']}{a}{cores['limpa']} e {cores['vermelho']}{b}{cores['limpa']}")

print(f"O nome é {cores['azul_claro']}{nome}{cores['limpa']}")
# \033[32m -> verde
# \033[31m -> vermelho