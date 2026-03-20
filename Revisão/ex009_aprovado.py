nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2
if media >= 7:
    print("APROVADO!")
    print("Parabéns, você conseguiu!")
elif media >= 6:
    print("RECUPERAÇÃO!")
    print("Ainda tem uma chance, boa sorte!")
else:
    print("REPROVADO!")
    print("Estude mais na próxima!")
