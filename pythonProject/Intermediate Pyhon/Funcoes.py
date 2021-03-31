'''
Funções - def em python
args and kwargs
'''

def funcao():
    print('Hello world!')

def funcao1(msg,nome):
    print(msg, nome)

funcao()
funcao()
funcao()
funcao()

funcao1('Olá','Lucas')
funcao1(nome='Olá',msg='Lucas')


def func(msg='mensagem',nome='nome'):
    return f'{msg} {nome}'


aux = func()
print(aux)


# sempre que eu seto um argumento padrão os próximos tambem tem que ser padrão ex
def gh(a1,a2=2,a3=3):
    print(a1,a2,a3)

gh('valor')

def tuple(*args):
    print(args)
    args = list(args)   #Mudando de tupla para list
    args[0] = 'Lucas'
    print(args)
    print(args[0])
    print(args[3])
    print(len(args))
tuple(1,2,3,4,5)


"""
Global
"""
var = 'lucas'
def fuun():
    print(var)
def fuuun():
    global var  #altera a variável global e não so a local
    var = 'edson'
    print(var)

print(var)
fuuun()
print(var)

