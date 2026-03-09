msg = input("Digite uma mensagem: ")

print("=======DESAFIO 004=======")

print(type(msg))
print("é alfanumérico?", msg.isalnum())
print("é alfabético?", msg.isalpha())
print("é numérico?", msg.isdigit())
print("está em minúsculas?", msg.islower())
print("está em maiúsculas?", msg.isupper())
print("Tem apenas espaço?", msg.isspace())
print("Está em título?", msg.istitle())
print("É imprimível?", msg.isprintable())