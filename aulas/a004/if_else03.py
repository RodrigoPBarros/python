n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
m = (n1 + n2) / 2

print(f"A média entre {n1} e {n2} é igual a {m:.1f}")

if m >= 6.0:
    print("Aluno aprovado!")
else:
    print("Aluno reprovado!")
print("Fim do programa.")