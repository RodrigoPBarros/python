resp = "S"
soma = quant = media = 0 = maior = menor = 0
while resp in "Ss":
    núm = int(input("Digite um número: "))
    soma += núm
    quant += 1 
    if quant == 1:
        maior = menor = núm
    else:
        if núm > maior:
            maior = núm
        if núm < menor:
            menor = núm
    resp = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
media = soma / quant
print(f"Voce digitou {quant} números e a media foi {media}")
if quant > 0:
    print(f"O maior número foi {maior} e o menor número foi {menor}")
else:
    print("Nenhum número foi digitado.")
