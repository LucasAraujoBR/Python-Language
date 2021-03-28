"""
Aula 12 - funções
"""
num1 = input('digite o primeiro numero INTEIRO: ')
num2 = input('digite o segundo numero INTEIRO: ')

if num1.isnumeric() and num2.isnumeric():
    print(f'a soma de {num1} + {num2} = {int(num1) + int(num2)}')
else:
    print(f'{num1} e {num2} são inválidos')


"""
TRY / EXCEPT
"""



try:
    print(f'a soma de {num1} + {num2} = {float(num1) + float(num2)}')
except:
    print('ERRO')