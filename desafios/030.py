n1 = int(input("Digite um número: "))
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
print("=======DESAFIO 030=======")

if n1 % 2 == 0:
    print(f"Seu número é par. {cores['verde']}✅{cores['limpa']}")
else:
    print(f"Seu número é ímpar. {cores['vermelho']}❌{cores['limpa']}")
print("Fim do programa")
