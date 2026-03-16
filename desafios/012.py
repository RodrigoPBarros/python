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
preço = float(input("Digite o preço do produto: "))
desconto = preço * 0.05
preço_com_desconto = preço - desconto
print("=======DESAFIO 012=======")
print(f"O preço original do produto é {cores['azul_claro']}R${preço:.2f}{cores['limpa']}.")
print(f"O desconto de 5% é {cores['vermelho']}R${desconto:.2f}{cores['limpa']}.")
print(f"O preço com desconto é {cores['verde']}R${preço_com_desconto:.2f}{cores['limpa']}.")
