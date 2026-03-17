
r1 = float(input("Digite o valor da primeria reta: "))
r2 = float(input("Digite o valor da segunda reta: "))
r3 = float(input("Digite o valor da terceira reta: "))

print("====== Desafio 035 ======")

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print("Sim, essas retas, podem formar um triângulo.")
else:
    print("Não, essas retas, não podem formar um triângulo.")
print("Fim do programa")