from random import randint
computador = randint(0,10)
print("Sou seu computador... Acabei de pensar em um número entr 0 e 10.")
print("Será que você consgue adivinhar qual foi?")
acertou = False
palpites = 0
while not acertou:
    jogador = int(input("Qual é seu palpite?"))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print("Mais... Tente mais uma vez.")
        elif jogador > computador:
            print("menos... Tente mais uma vez.")
print(f"Acertou com {palpites} palpites")