import random
import string

# Pergunta as configurações da senha
tamanho = int(input("Quantos caracteres na senha? "))
usar_maiusculas = input("Quer letras maiúsculas? (s/n) ").lower() == 's'
usar_numeros = input("Quer números? (s/n) ").lower() == 's'
usar_simbolos = input("Quer símbolos? (s/n) ").lower() == 's'

# Aqui fazemos a base da senha
caracteres = string.ascii_lowercase  # letras minúsculas sempre
if usar_maiusculas:
    caracteres += string.ascii_uppercase
if usar_numeros:
    caracteres += string.digits
if usar_simbolos:
    caracteres += string.punctuation

# Gera a senha
senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
print("🔑 Sua senha gerada: ", senha)
