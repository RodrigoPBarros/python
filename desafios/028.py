import random
n1 = random.randint(0, 5)
n2 = int(input("Digite um número entre 0 e 5: "))

print("=======DESAFIO 028=======")

if n1 ==n2:
    print("Parabéns, você acertou!")
else:
    print(f"Você errou, o número era {n1}")
print("Fim do programa")