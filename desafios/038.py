n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))

print("====== Desafio 38 ======")
if n1 > n2:
    print(f"O primero Valor é maior ({n1:.2f})")
elif n2 > n1:
    print(f"O segundo valor é maior ({n2:.2f})")
else:
    print("Não existe valor maior, os dois são iguais.")
