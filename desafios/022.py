cores = {
    "limpa": "\033[m",
    "verde": "\033[32m",
    "vermelho": "\033[31m",
    "azul": "\033[34m",
    "azul_claro": "\033[36m",
    "amarelo": "\033[33m",
    "roxo": "\033[35m",
    "branco": "\033[37m"
}
nome = input("Digite seu nome: ")
maiuscula = nome.upper()
minuscula = nome.lower()
semespaço = nome.replace(" ", "")
tamanho = len(nome)

print("=======DESAFIO 022=======")

print(f"Seu nome em maiúsculas é: {cores['azul']}{maiuscula}{cores['limpa']}")
print(f"Seu nome em minúsculas é: {cores['vermelho']}{minuscula}{cores['limpa']}")
print(f"Seu nome sem espaços é: {cores['verde']}{semespaço}{cores['limpa']}")
print(f"O tamanho do seu nome é: {cores['roxo']}{tamanho}{cores['limpa']}")