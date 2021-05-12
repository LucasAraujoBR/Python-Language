"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês.
"""


try:
    hora = input('Quanto você ganha por hora ? ')
    hora = float(hora)
    totalHoras = input('Quantas horas você trabalha no mês ? ')
    totalHoras = float(totalHoras)
    print(f'Trabalhando {totalHoras} horas por mês, recebendo {hora} pela hora, você recebera R$:{totalHoras*hora} por mês.')

except:
    print('Dados inválidos')