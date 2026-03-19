n1 = float(input("Digite o Primeiro número: "))
n2 = float(input("Digite o Segundo número: "))
opcao = 0
while opcao != "5":
    print('''        [1]Somar
        [2]Multiplicar
        [3]Maior
        [4]Novos Número
        [5]Sair do programa''')
    opcao = str(input("Qual sua opção? "))
    if opcao == "1":
        soma = n1 + n2 
        print(f"A soma de {n1} e {n2} é {soma}")
    elif opcao == "2":
        multiplicacao = n1 * n2
        print(f"A multiplicação de {n1} e {n2} é {multiplicacao}")
    elif opcao == "3":
        if n1 > n2:
            print(f"{n1} é maior que {n2}")
        elif n2 > n1:
            print(f"{n2} é maior que {n1}")
        else:
            print("Os dois números são iguais")
    elif opcao == "4":
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
    elif opcao == "5":
        print("Fim do programa! Volte Sempre! ")
        