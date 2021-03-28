"""
Aula 7 - Formatação de strings
"""
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
#Inicio da aula 7!
print(f'{nome} tem {altura} de altura e {peso} kg, isso gera o imc {imc:.2f}')
print('{} tem {} de altura e {} kg, isso gera o imc {:.2f}'.format(nome,altura,peso,imc))
print('{1}{0}{1} tem {1} de altura e {2} kg, isso {2} gera o imc {3}'.format(nome,altura,peso,imc)) #agora sempre posso repetir
print('{a}{z}{a} tem {a} de altura e {b} kg, isso {b} gera o imc {c}'.format(a=nome,b=altura,c=peso,z=imc)) #agora sempre posso repetir usando as variaveis que denominei