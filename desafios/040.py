nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2

print("====== Desafio 040 ======")
if media < 5:
    print("Reprovado")
elif media >= 5 and media <= 5.9:
    print("Recuperação")
else:
    print("Aprovado")
print("Média: ", media)
print("Fim do programa")