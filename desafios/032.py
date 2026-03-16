
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
ano = int(input("Digite o ano: "))
print("=======DESAFIO 032=======")
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"O ano é bissexto. {cores['verde']}✅{cores['limpa']}")
else:
    print(f"O ano não é bissexto. {cores['vermelho']}❌{cores['limpa']}")
print("Fim do Programa.")