nome = str(input('Digite seu nome: '))
if nome == "Rodrigo":
    print("Que nome lindo!")
elif nome == "Maria" or nome == "João":
    print("Que nome popular!")
elif nome in "Ana Claúdia Jéssica Juliana":
    print("Que nome feminino!")
else:
    print("Que nome comum!")
print(f"Tenha um bom dia, {nome}!")