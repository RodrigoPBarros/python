n = 0
s = 0
quant = 0
while n != 999:
    n = int(input("Digite um valor inteiro(999 PARA): "))
    if n == 999:
        break
    s += n
    quant +=1

print(f"A quantidade de números digitados foi: {quant}")
print(f"A soma dos números é: {s}")