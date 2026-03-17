idade = int(input("Digite a idade: "))

print("====== Desafio 041 ======")
if idade < 0:
    print("Idade inválida!")
else:
    if idade <= 9:
        categoria = "Mirim"
    elif idade <= 13:
        categoria = "Infantil"
    elif idade <= 19:
        categoria = "Junior"
    else:
        categoria = "Master"

    print(f"Categoria: {categoria} (idade {idade})")
print("Fim do desafio 041")