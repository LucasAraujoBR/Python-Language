"""
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo.
"""

try:
    num = input('Digite um número inteiro: ')
    num = int(num)
    num1 = input('Digite outro número inteiro: ')
    num1 = int(num1)
    numReal = input('Digite um número Real: ')
    numReal = int(numReal)
    if num>0 and num1>0:
        print(f'O produto do dobro do primeiro com metade do segundo: {(num+num)*(num1/2):.2f}')
        print(f'a soma do triplo do primeiro com o terceiro: {(3*num)+(numReal):.2f}')
        print(f'o terceiro elevado ao cubo: {numReal**3}')
    else:
        print('Dados inválidos')


except:
    print('Dados inválidos')