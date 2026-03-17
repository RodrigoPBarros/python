
r1 = float(input("Digite o valor da primeria reta: "))
r2 = float(input("Digite o valor da segunda reta: "))
r3 = float(input("Digite o valor da terceira reta: "))
isosceles = r1 == r2 or r1 == r3 or r2 == r3
equilatero = r1 == r2 == r3
escaleno = not isosceles and not equilatero

print("====== Desafio 042 ======")

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print("As retas formam um triângulo")
    if equilatero:
        print("O triângulo é equilátero")
    elif isosceles:
        print("O triângulo é isósceles")
    elif escaleno:
        print("O triângulo é escaleno")
else:
    print("As retas não formam um triângulo")
print("Fim do programa")

