preço = float(input("Digite o preço do produto: "))
desconto = preço * 0.05
preço_com_desconto = preço - desconto
print("=======DESAFIO 012=======")
print(f"O preço original do produto é R${preço:.2f}.")
print(f"O desconto de 5% é R${desconto:.2f}.")
