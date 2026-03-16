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
frase = input('Digite uma frase: ').strip()

print("=======DESAFIO 026=======")

print(f"A letra 'A' aparece {cores['verde']}{frase.lower().count('a')}{cores['limpa']} vezes na frase.")
print(f"A primeira letra 'A' aparece na posição {cores['verde']}{frase.lower().find('a') + 1}{cores['limpa']}.")
print(f"A última letra 'A' aparece na posição {cores['verde']}{frase.lower().rfind('a') + 1}{cores['limpa']}.")