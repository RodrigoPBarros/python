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
km = float(input("Digite a quantos quilometros por hora você está: "))

print("=======DESAFIO 029=======")

if km > 80:
    multa = (km - 80) * 7
    print("Você foi multado por excesso de velocidade.")
    print(f"Sua multa é de R${multa:.2f}.")
else:
    print("Você está dentro do limite de velocidade.")
print("Fim do Programa.")
