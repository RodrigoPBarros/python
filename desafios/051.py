print("===== DESAFIO 051 =====")
p = int(input("Digite o primeiro termo da PA: "))
r = int(input("Digite a razão da PA: "))
print("Os 10 primeiros termos da PA são: ")
for i in range(10):
    print(p, end=" → ")
    p += r
print("FIM")
