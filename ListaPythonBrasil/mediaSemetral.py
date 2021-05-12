"""
Faça um Programa que peça as 4 notas bimestrais e mostre a média.
"""


try:
    nota1 = input('Digite a primeira nota: ')
    nota1 = float(nota1)
    nota2 = input('Digite a segunda nota: ')
    nota2 = float(nota2)
    nota3 = input('Digite a terceira nota: ')
    nota3 = float(nota3)
    nota4 = input('Digite a quarta nota: ')
    nota4 = float(nota4)
    print(f'Notas\n1-{nota1}\n2-{nota2}\n3-{nota3}\n4-{nota4}')
    print()
    print(f'Sua média é {(nota1+nota2+nota3+nota4)/4}')
except:
    print('Valores inválidos')