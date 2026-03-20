n1 = (int(input('Digite um número(Digite 999 para parar): ')))
n2 = 0
c = 0 
while n1 != 999:
    n2 += n1
    c += 1 
    n1 = int(input('Digite um número(Digite 999 para parar): '))
print(f"Foram digitados {c} números e a soma entre eles é {n2}")