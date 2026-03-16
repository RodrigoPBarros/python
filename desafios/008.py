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
metros = float(input("Digite a distância em metros: "))
centimetros = metros * 100
milimetros = metros * 1000
print("=======DESAFIO 008=======")
print(f"{metros} metros equivalem a {centimetros:.2f} centímetros e {milimetros:.2f} milímetros.")