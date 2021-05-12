"""
Faça um Programa que converta metros para centímetros.
"""

try:
    valor = input('Digite a quantidades de Metros que quer converter para CM: ')
    valor = float(valor)
    print(f'{valor} M = {valor*100} CM')
except:
    print('Dados inválidos')