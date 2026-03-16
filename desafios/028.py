import random
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
n1 = random.randint(0, 5)
n2 = int(input("Digite um número entre 0 e 5: "))

print("=======DESAFIO 028=======")

if n1 ==n2:
    print(f"Parabéns, você acertou! {cores['verde']}🎉{cores['limpa']}")
else:
    print(f"Você errou, o número era {cores['vermelho']}{n1}{cores['limpa']}")
print("Fim do programa")