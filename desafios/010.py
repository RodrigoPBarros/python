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
reais = float(input('Digite quantos reais você tem na carteira: '))
dolar = reais / 5.22
euro = reais / 6.06
libra = reais / 7.01

print("=======DESAFIO 010=======")

print(f"Com {cores['azul_claro']}R${reais:.2f}{cores['limpa']} você pode comprar {cores['verde']}US${dolar:.2f}{cores['limpa']}, {cores['verde']}€{euro:.2f}{cores['limpa']} ou {cores['verde']}£{libra:.2f}{cores['limpa']}.")