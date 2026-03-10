nome = input("Digite seu nome: ")
maiuscula = nome.upper()
minuscula = nome.lower()
semespaço = nome.replace(" ", "")
tamanho = len(nome)

print("=======DESAFIO 009=======")

print(f"Seu nome em maiúsculas é: {maiuscula}")
print(f"Seu nome em minúsculas é: {minuscula}")
print(f"Seu nome sem espaços é: {semespaço}")
print(f"O tamanho do seu nome é: {tamanho}")