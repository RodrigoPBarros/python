import random
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
aluno1 = input('Digite o nome do primeiro aluno: ')
aluno2 = input('Digite o nome do segundo aluno: ')  
aluno3 = input('Digite o nome do terceiro aluno: ')
aluno4 = input('Digite o nome do quarto aluno: ')
lista = [aluno1, aluno2, aluno3, aluno4]
escolhido = random.choice(lista)

print("=======DESAFIO 020=======")
print(f"A ordem de apresentação será: {cores['azul_claro']}{random.sample(lista, k=4)}{cores['limpa']}.")
