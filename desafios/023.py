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
N1 = int(input("Digite um número de 0 até 9999: "))
u = N1 // 1 % 10
d = N1 // 10 % 10
c = N1 // 100 % 10
m = N1 // 1000 % 10

print("=======DESAFIO 023=======")

print(f"Analisando o número {N1}...")
print(f"Unidade: {cores['vermelho']}{u}{cores['limpa']}")  
print(f"Dezena: {cores['verde']}{d}{cores['limpa']}")
print(f"Centena: {cores['azul']}{c}{cores['limpa']}")
print(f"Milhar: {cores['roxo']}{m}{cores['limpa']}")