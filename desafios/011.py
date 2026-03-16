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
largura = float(input("Digite a largura da parede em metros: "))
altura = float(input("Digite a altura da parede em metros: "))
area = largura * altura
tinta = area / 2
print("=======DESAFIO 011=======")
print(f"A área da parede é de {cores['azul_claro']}{area:.2f}{cores['limpa']} metros quadrados.")
print(f"A quantidade de tinta necessária para pintar a parede é de {cores['verde']}{tinta:.2f}{cores['limpa']} litros.")