preço = float(input('Digite o preço do produto: R$ '))
pagamento = int(input('''Escolha a forma de pagamento:
[1] À vista dinheiro/cheque
[2] À vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão
Digite a opção: '''))

print("====== Desafio 044 ======")
if pagamento == 1:
    print(f'Preço final: R$ {preço * 0.9:.2f} (10% de desconto)')
elif pagamento == 2:
    print(f'Preço final: R$ {preço * 0.95:.2f} (5% de desconto)')
elif pagamento == 3:
    print(f'Preço final: R$ {preço:.2f} (preço normal)')
elif pagamento == 4:
    print(f'Preço final: R$ {preço * 1.2:.2f} (20% de juros)')
else:
    print('Opção inválida. Tente novamente.')