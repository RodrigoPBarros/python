km = float(input("Digite a distância em quilômetros: "))
dias = int(input("Digite o número de dias: "))
preco_km = 0.50
preco_dia = 60.00  
custo_km = km * preco_km
custo_dia = dias * preco_dia
custo_total = custo_km + custo_dia

print("======Resultado======")

print(f"A distância percorrida é {km:.2f} km.")
print(f"O número de dias é {dias} dia(s).")
print(f"O custo por km é R${preco_km:.2f}.")
print(f"O custo por dia é R${preco_dia:.2f}.")
print(f"O custo total do aluguel é R${custo_total:.2f}.")
