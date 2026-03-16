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
salario = float(input('Digite o salário do funcionário: R$ '))
if salario <=1250:
    aumento = salario *0.15
else:
    aumento = salario * 0.10

print(f'O funcionário que ganhava R$ {cores["azul_claro"]}{salario:.2f}{cores["limpa"]} passa a ganhar R$ {cores["verde"]}{salario + aumento:.2f}{cores["limpa"]} com o aumento de R$ {cores["amarelo"]}{aumento:.2f}{cores["limpa"]}.')