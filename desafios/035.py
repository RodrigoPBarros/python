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
r1 = float(input("Digite o valor da primeria reta: "))
r2 = float(input("Digite o valor da segunda reta: "))
r3 = float(input("Digite o valor da terceira reta: "))

print("====== Desafio 035 ======")

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print(f"Sim, essas retas, podem formar um triângulo. {cores['verde']}✅{cores['limpa']}")
else:
    print(f"Não, essas retasn, não podem formar um triângulo. {cores['vermelho']}❌{cores['limpa']}")
print("Fim do programa")