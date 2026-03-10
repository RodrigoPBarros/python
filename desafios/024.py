cidade = input('Digite o nome da cidade: ').strip()

print("=======DESAFIO 010=======")

print(f"A cidade {cidade} começa com 'Santo'? {cidade[:5].lower() == 'santo'}")