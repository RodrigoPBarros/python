numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite outro número: "))
numero3 = int(input("Digite apenas mais um número: "))

if numero1 > numero2 and numero1 > numero3:
    print(f"{numero1} é o maior número.")
elif numero2 > numero1 and numero2 > numero3:
    print(f"{numero2} é o maior número.")
else:
    print(f"{numero3} é o maior número.")
