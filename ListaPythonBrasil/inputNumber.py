"""
Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
"""

try:
    num = input('Digite um número')
    num = int(num)
    print(num)
except:
    print('Valor digitado difere de número')