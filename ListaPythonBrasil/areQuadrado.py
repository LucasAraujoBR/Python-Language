"""
Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
A = b. h
"""

try:
    base = input('Digite a base: ')
    base = float(base)
    altura = input('Digite a altura: ')
    altura = float(altura)
    print(f'A área do quadrado de base={base} e altura={altura} eh: {base*altura}')
    print(f'O dobro da área={base*altura} eh: {(base*altura)*2}')
except:
    print('Dados inválidos')