"""
Aula 10 - Condicionais IF, ELIF e ELSE
"""
if False:
    print("Verdadeiro.")
elif True:
    print("Agora é verdadeiro")
    name = input("Whats your name? ")
    print(name)
elif True:
    print("Agora continua verdadeiro")
else:
    print("Falso.")

"""
Operadores relacionais em Python
=   Atribuição de valor
==  Igualdade
>   Maior que 
>=  Maior ou igual que
<   Menor que
<=  Menor ou igual que
!=  Diferente
"""

name = input('whats your name? ')
age = input('whats your age? ')

if int(age)>=18:
    print("Welcome to the casino")
else:
    print("Your no have 18 years old.")


if int(age)<=20:
    print(f'{name} too young for drinks')
elif int(age)<=25:
    print(f'{name} you can have a drink')
else:
    print(f'{name} are you kidding me? bitch')


"""
Operadores lógicos 
and - e
or - ou
not - não
in - está contido
not in - não está contido
if - se
"""

a = input('valor de a')
nome = 'lucas'
if not a:
    print("Favor preencha o valor de A")
#está contido
if 'u' in nome:
    print(f"U está contido em {nome}")
else:
    print(f'não existe em {nome}')

#Não está contigo
if 'k' not in nome:
    print(f"K não esta contido em {nome}")


"""
exemplo básico de usuario e senha
"""
login = input("Whats your nickname? ")
senha = int(input(f'Whats your password? '))

if login == 'jujuba' and senha == 1234:
    print(f'{login} conectado')
elif login != 'jujuba' and senha == 1234:
    print(f'Login incorreto!')
elif login == 'jujuba' and senha != 1234:
    print("Senha Inválida")
else:
    print("Dados errados!")
