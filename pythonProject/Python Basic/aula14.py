"""
aula 14 - formatando valores em python
"""


"""
:s - Texto (string)
:d - Inteiros (int)
:f - Números de ponto flutuante (float)
:.(Número)f - quantidade de casas decimais (float)
:(Caractere)(> ou < ou ^)(quantidade)(TIPO - s, d ou f)

> - Esquerda
< - Direita
^ - Centro
"""

num = 5
num2 = 2

print(f'{num/num2:.2f}')
print(f'{num:0>10}')
num3 = 1050

print(f'{num3:0>10}')
print(f'{num3:0<10}')
print(f'{num3:.2f}')

nome = 'lucas araujo'
print((50-len(nome))/2)

print(f'{nome:#^50}')

nome_formatado = '{:@>50}'.format(nome)
nome_formatado2 = '{n:@>50}{n}{n}'.format(n=nome)
print(nome_formatado)
print(nome_formatado2)

print(nome.lower()) #Minusculo
print(nome.upper()) #Maiusculo
print(nome.title()) #Primeiras letras maiusculas

