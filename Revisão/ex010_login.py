usuario_correto = "Rodrigo"
senha_correta = "123456"
usuario = input("Digite seu usuário: ")
senha = input("Digite sua senha: ")

if usuario == usuario_correto and senha == senha_correta:
    print("Bem-vindo!")
else:
    print("Login inválido!")