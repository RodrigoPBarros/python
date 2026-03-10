largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
area = largura * altura
tinta = area / 2

print("======Resultado======")
print(f"A área da parede é {area:.2f} metros quadrados.")
print(f"A quantidade de tinta necessária para pintar a parede é {tinta:.2f} litros.")
