N1 = int(input("Digite um número de 0 até 9999: "))
u = N1 // 1 % 10
d = N1 // 10 % 10
c = N1 // 100 % 10
m = N1 // 1000 % 10

print("=======DESAFIO 023=======")

print(f"Analisando o número {N1}...")
print(f"Unidade: {u}")  
print(f"Dezena: {d}")
print(f"Centena: {c}")
print(f"Milhar: {m}")