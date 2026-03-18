print("===== DESAFIO 054 =====")
from datetime import date

atual = date.today().year
maior = 0
for i in range(1, 8):
    nasc = int(input(f"Digite o ano de nascimento da {i}ª pessoa: "))
    idade = atual - nasc
    if idade >= 18:
        maior += 1
print(f"Das 7 pessoas, {maior} são maiores de idade.")
print("===== FIM =====")