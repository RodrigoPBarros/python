reais = float(input('Digite quantos reais você tem na carteira: '))
dolar = reais / 5.22
euro = reais / 6.06
libra = reais / 7.01
print("=======DESAFIO 008=======")
print(f"Com R${reais:.2f} você pode comprar US${dolar:.2f}, €{euro:.2f} ou £{libra:.2f}.")