"""
Primeiro Script pós formatação // Mini calculadora 
"""


print('Begin the program')
print()
print('Mini Calculadora')
print('Menu')
print('1 - Somar')
print('2 - Subtrair')
print('3 - Multiplicar')
print('4 - Dividir')
var = input('Digite o código correspondente a operação: ')
try:
    var = int(var)
except:
    print('Dados inválidos, programa encerrado!')
while var<0 or var>4:
    print('Menu')
    print('1 - Somar')
    print('2 - Subtrair')
    print('3 - Multiplicar')
    print('4 - Dividir')
    var = input('Digite o código correspondente a operação: ')
    var = int(var)
if var == 1:
    print('------------------------------------------------')
    print('Você escolheu soma.')
    valor1 = input('Digite um valor: ')
    valor2 = input('Digite outro valor: ')
    valor1 = int(valor1)
    valor2 = int(valor2)    
    print(f'{valor1} + {valor2} = {valor1+valor2}')
elif var == 2:
    print('------------------------------------------------')
    print('Você escolheu subtração.')
    valor3 = input('Digite um valor: ')
    valor4 = input('Digite outro valor: ')
    valor3 = int(valor3)
    valor4 = int(valor4)
    print(f'{valor3} - {valor4} = {valor3-valor4}') 
elif var == 3:
    print('------------------------------------------------')
    print('Você escolheu multiplicação.')
    valor5 = input('Digite um valor: ')
    valor6 = input('Digite outro valor: ')
    valor5 = int(valor5)
    valor6 = int(valor6)
    print(f'{valor5} * {valor6} = {valor5*valor6}')
elif var == 4:
    print('------------------------------------------------')
    print('Você escolheu divisão.')
    valor7 = input('Digite um valor: ')
    valor8 = input('Digite outro valor: ')
    valor7 = int(valor7)
    valor8 = int(valor8)
    print(f'{valor7} / {valor8} = {valor7/valor8}')
else:
    print('Dados inválidos, programa encerrado!')   
