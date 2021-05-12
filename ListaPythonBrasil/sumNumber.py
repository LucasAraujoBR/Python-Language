"""
Faça um Programa que peça dois números e imprima a soma.
"""
try:
    num = input('Digite um número: ')
    num2 = input('Digite outro número: ')
    num = int(num)
    num2 = int(num2)
    print(f'{num} + {num2} = {num+num2}')
except:
    print('Valores inválidos')