frase = "Curso em video Python"
len(frase) # conta os caracteres da string, incluindo os espaços
frase.count('o') # conta quantas vezes a letra 'o' aparece na string
frase.count('o', 0, 13) # conta quantas vezes a letra 'o' aparece na string, do caractere 0 ao 12
frase.find('deo') # encontra a posição onde começa a string 'deo'
frase.rfind('o') # encontra a posição onde termina a string 'o'
frase.replace('Python', 'Android') # substitui a string 'Python' por 'Android'
frase.upper() # transforma a string em maiúscula
frase.lower() # transforma a string em minúscula
frase.capitalize() # transforma a primeira letra da string em maiúscula e as demais em minúscula
frase.title() # transforma a primeira letra de cada palavra da string em maiúscula  
frase.strip() # remove os espaços em branco do início e do fim da string
frase.rstrip() # remove os espaços em branco do fim da string
frase.lstrip() # remove os espaços em branco do início da string
frase.split() # divide a string em uma lista de palavras
'-'.join(frase) # junta os caracteres da string com o separador '-'
