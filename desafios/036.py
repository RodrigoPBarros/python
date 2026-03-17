valor_casa = float(input('Valor da casa: R$ '))
salario = float(input("Salário do comprador: R$ "))
anos = int(input("Quantos anos de financiamento? "))

prestacao = valor_casa / (anos * 12)
limite = salario * 0.3

print("====== Desafio 036 ======")

print(f"Para pagar uma casa de R$ {valor_casa:.2f} em {anos}:")
print(f"Prestação mensal: R$ {prestacao:.2f}")
print(f"Limite de prestação: R$ {limite:.2f}")

if prestacao > limite:
    print("Empréstimo Negado!")
else:
    print("Empréstimo Aprovado!")
print("Fim do programa")