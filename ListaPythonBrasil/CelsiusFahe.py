"""
Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
C = 5 * ((F-32) / 9).
"""

try:
    Fahrenheit = input('Digite a temperatura em graus Fahrenheit:  ')
    Fahrenheit = float(Fahrenheit)
    conversor = ((Fahrenheit-32)*5)/9
    print(f'{Fahrenheit} Fahrenehit equivale a {conversor:.2f} Celsius.')

except:
    print('Dados inválidos.')


"""
Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
"""

try:
    Celsius = input('Digite a temperatura em graus Celsius:  ')
    Celsius = float(Celsius)
    conversor = (Celsius * 9/5) + 32
    print(f'{Celsius} Celsius equivale a {conversor:.2f} Fahrenheit.')

except:
    print('Dados inválidos.')