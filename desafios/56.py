soma_idade = 0
maior_idade_homem = 0
nome_velho = ''
mulheres_20 = 0

for i in range(1, 5):
    print(f"----- {i}ª PESSOA -----")
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).strip().upper()
    
    soma_idade += idade
    
    # Lógica do homem mais velho
    if i == 1 and sexo == 'M': # Se for o primeiro homem
        maior_idade_homem = idade
        nome_velho = nome
    if sexo == 'M' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_velho = nome
        
    # Lógica das mulheres novas
    if sexo == 'F' and idade < 20:
        mulheres_20 += 1

media = soma_idade / 4
print(f"A média de idade é {media} anos.")
print(f"O homem mais velho tem {maior_idade_homem} anos e se chama {nome_velho}.")
print(f"Ao todo são {mulheres_20} mulheres com menos de 20 anos.")
print("===== FIM =====")