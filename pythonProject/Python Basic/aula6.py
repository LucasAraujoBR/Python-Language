"""
Aula 6 - Variáveis
"""

nome = 'lucas'
idade = 22
altura = 1.82
maiorIdade = idade > 18
peso = 113
print("Name",nome)
print("Age:",idade)
print("Altura:",altura)
print("Bool:",maiorIdade)

## Operações matemáticas
print(idade * altura)

#Exemplo calculo do IMC
imc = peso / altura ** 2

print(nome," tem a altura", altura,"e peso",peso,"seu IMC é:",imc)
