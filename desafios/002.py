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

dia = int(input("Digite o dia do seu nascimento: "))
mes = str(input("Digite o mês do seu nascimento: "))
ano = int(input("Digite o ano do seu nascimento: "))

print("=======DESAFIO 002=======")
print(
    f"Você nasceu no dia {cores['azul_claro']}{dia}{cores['limpa']} "
    f"do mês {cores['azul_claro']}{mes}{cores['limpa']} "
    f"do ano de {cores['azul_claro']}{ano}{cores['limpa']}."
)