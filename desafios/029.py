km = float(input("Digite a quantos quilometros por hora você está: "))

print("=======DESAFIO 029=======")

if km > 80:
    multa = (km - 80) * 7
    print("Você foi multado por excesso de velocidade.")
    print(f"Sua multa é de R${multa:.2f}.")
else:
    print("Você está dentro do limite de velocidade.")
print("Fim do Programa.")
