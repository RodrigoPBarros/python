s = 0
n = 0
while n != 999:
    n = int(input("Digite um número: "))
    if n == 999:
        break
    s += n
print(f"Soma vale {s}")