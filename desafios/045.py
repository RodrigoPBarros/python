escolha = input('Escolha pedra, papel ou tesoura: ').lower()
jokenpo = ['pedra', 'papel', 'tesoura']
print("====== Desafio 045 ======")
if escolha not in jokenpo:
    print('Opção inválida. Por favor, escolha pedra, papel ou tesoura.')
else:
    import random
    computador = random.choice(jokenpo)
    print(f'Computador escolheu: {computador}')

    if escolha == computador:
        print('Empate!')
    elif (escolha == 'pedra' and computador == 'tesoura') or (escolha == 'papel' and computador == 'pedra') or (escolha == 'tesoura' and computador == 'papel'):
        print('Você venceu!')
    else:
        print('Você perdeu!')
print('Fim do jogo.')