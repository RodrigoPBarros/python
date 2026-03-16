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
salario = float(input("Digite o salário do funcionário: "))
aumento = salario * 0.15
salario_com_aumento = salario + aumento
print("=======DESAFIO 013=======")
print(f"O salário original do funcionário é {cores['azul_claro']}R${salario:.2f}{cores['limpa']}.")
print(f"O aumento de 15% é {cores['vermelho']}R${aumento:.2f}{cores['limpa']}.")
print(f"O salário com aumento é {cores['verde']}R${salario_com_aumento:.2f}{cores['limpa']}.")
