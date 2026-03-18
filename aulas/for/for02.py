n = int(input("Digite um número inteiro: "))
i = int(input("Início:"))
f = int(input("Fim:"))
p = int(input("Passo:"))
for c in range(1, n+1):
    print(c)
print("Fim")

for c in range(i, f+1, p):
    print(c)
print("Fim")