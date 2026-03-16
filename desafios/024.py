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
cidade = input("Digite o nome de uma cidade: ").strip()
print("======Desafio 024======")

começa_santo = cidade[:5].lower() == 'santo'

print(f"A cidade {cidade} começa com 'Santo'? {cores['verde']}{começa_santo}{cores['limpa']}")
