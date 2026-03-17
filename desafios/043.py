peso = float(input('Digite o peso da pessoa: '))
altura = float(input('Digite a altura da pessoa: '))
imc = peso / (altura ** 2)

print("====== Desafio 043 ======")

if imc < 18.5:
    print("A pessoa está abaixo do peso.")
elif imc < 25:
    print("A pessoa está com o peso ideal.")
elif imc < 30:
    print("A pessoa está com obesidade.")
elif imc < 40:
    print("A pessoa está com obesidade mórbida.")
else:
    print("A pessoa está com obesidade mórbida grave.")
