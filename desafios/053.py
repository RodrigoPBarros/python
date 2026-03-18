print("===== DESAFIO 053 (Inversão Visual) =====")
frase = str(input("Digite uma frase: ")).strip().upper()

# Inverte a frase inteira, inclusive os espaços
inverso = frase[::-1]

print(f"O original é: {frase}")
print(f"O inverso é:  {inverso}")

if frase == inverso:
    print("É um palíndromo perfeito (com espaços e tudo)!")
else:
    print("Não é um palíndromo com espaços, mas talvez seja sem eles!")
# Agora vamos remover os espaços para verificar o palíndromo sem eles
frase_sem_espacos = frase.replace(" ", "")
inverso_sem_espacos = frase_sem_espacos[::-1]
if frase_sem_espacos == inverso_sem_espacos:
    print("É um palíndromo sem considerar os espaços!")
else:
    print("Não é um palíndromo mesmo sem considerar os espaços.")   
    