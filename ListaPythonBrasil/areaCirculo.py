"""
Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
"""
'''
AreaC = PI.R^2
PI = 3.14
'''
try:
    PI = 3.14
    raio = input('Digite o Raio de um cículo:  ')
    raio = float(raio)
    print(f'O círculo de Raio {raio} tem {PI*(raio**2)} de área.')
except:
    print('Dados inválidos')