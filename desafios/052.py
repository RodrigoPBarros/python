print("===== DESAFIO 052 =====")
n = int(input("Digite um número: "))
c = 0
for i in range(1, n + 1):
    if n % i == 0:
        c += 1
if c == 2:
    print(f"{n} é um número primo.")
else:
    print(f"{n} não é um número primo.")
print("===== FIM =====")