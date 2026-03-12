salario = float(input('Digite o salário do funcionário: R$ '))
if salario <=1250:
    aumento = salario *0.15
else:
    aumento = salario * 0.10

print(f'O funcionário que ganhava R$ {salario:.2f} passa a ganhar R$ {salario + aumento:.2f} com o aumento de R$ {aumento:.2f}.')