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
print("=======DESAFIO 031=======")
distancia = float(input('Digite a distância da viagem em km: '))

if distancia <= 200:
    preco = distancia * 0.50
else: 
    preco = distancia * 0.45

print(f'O preço da passagem é {cores["verde"]}R${preco:.2f}{cores["limpa"]}')
print("Fim do programa")
