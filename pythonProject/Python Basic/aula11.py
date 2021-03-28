"""
Aula 11 - len - Quantidade de caracteres
"""

nome = input('digite o nome: ')
print(f'{nome} tem {len(nome)} caracteres')


if len(nome)<6:
    print("Você precisa digitar pelo menos 6 caracteres")
else:
    print("Congratulations")
