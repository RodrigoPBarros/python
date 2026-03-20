n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))
opcao = 0
while opcao != "6":
    print('''        [1]Somar
        [2]Subtrair
        [3]Multiplicar
        [4]dividir
        [5]Novos Número
        [6]Sair do programa''')
    opcao = str(input("Qual sua opção? "))
    if opcao == "1":
        soma = n1 + n2
        print(f"A soma de {n1} mais {n2} é {soma:.2f}")
    elif opcao == "2":
        sub = n1 - n2
        print(f"A subtração de {n1} menos {n2} é {sub:.2f}")
    elif opcao == "3":
        mult = n1 * n2
        print(f"A multiplicação de {n1} vezes {n2} é {mult:.2f}")
    elif opcao == "4":
        div = n1 / n2
        print(f"A divisão de {n1} por {n2} é {div:.2f}")
    elif opcao == "5":
        n1 = float(input("Digite um número: "))
        n2 = float(input("Digite outro número: "))
    else:
        print("Fim do programa! Volte Sempre!")
