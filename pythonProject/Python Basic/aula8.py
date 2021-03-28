"""
Aula 8 - Desafio prático
"""
"""
*Criar variáveis para nome(str), idade(int)
*altura(float) e peso(float) de uma pessoa 
*cria variável com o ano atual (int)
*obtem o ano de nascimento da pessoa (baseado na idade e no ano atual)
*obtem o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa)
*Exibir um texto com todos os valores na tela usando F-strings (Com as chaves)
"""

name = 'José Falcão de Almeida'
age = 38
weight = 120.5
height = 1.95
currentYear = 2021
yearOfBirth = currentYear - age
imc = weight/height**2
print(f"The year of {name}'s birth is {yearOfBirth}")
print(f'{name} is {height} tall and has {weight} KG, generating {imc:.2f} IMC.')
print(f'Name: {name} \nAge: {age} \nWeight: {weight} \nHeight: {height} \nCurrent Year: {currentYear} \nYear of Birth: {yearOfBirth} \nIMC: {imc:.2f}')