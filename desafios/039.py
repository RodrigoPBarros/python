ano = int(input("Digite o ano que você nasceu: "))

print("====== Desafio 039 ======")
if 2026 - ano < 18:
    print("Você ainda não pode se alistar")
    print(f"Ainda faltam {18 - (2026 - ano)} anos para o alistamento")
elif 2026 - ano >= 18:
    print("Você deve se alistar esse ano")
else: 
    print(f"Passaram {(2026 - ano) - 18} anos do seu alistamento")
    print("Você já deveria ter se alistado")
print("Fim do programa")