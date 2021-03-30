"""
Operadores Ternários em python
"""
log = False
msg = 'Logado.' if log else "don't logged."
print(msg)


age = 18

maiorAge = (age >= 18)
msg2 = 'Logado' if maiorAge else 'negado'
print(msg2)


"""
Expressão condicional com operador OR
"""

name = input('Qual seu nome? ')
if name:
    print(name)
else:
    print('Você não digitou nada')


# ou posso encurtar assim
print(name or 'Você não digitou nada')


a = 0
b = None
c = False
d = []
e = {}
f = 22
g = 'Lucas'

print(a or b or c or d or e or f or g)