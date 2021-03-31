"""
1 - Crie uma função que exibe uma saudação com os parâmetros saudacao e nome.
"""
def saudacao(saud,nome):
    print(f'{saud} {nome}')

saudacao('Olá','Lucas')

"""
2 - Crie uma função que recebe 3 números como parâmetros e exiba a soma entre 
eles.
"""
def soma3num(num1,num2,num3):
    print(f'{num1} + {num2} + {num3} = {num1+num2+num3}')

soma3num(1,2,3)
soma3num(-1,-2,-3)


"""
3 - Crie uma função que receba 2 números. O primeiro é um valor e o segundo um
percentual (ex. 10%). Retorne (return) o valor do primeiro número somado
do aumento do percentual do mesmo.
"""

def aumento(valor,percentual):
    valorPercentual = percentual / 100
    qtdAumento = valor * valorPercentual
    resultado = valor + (valor * valorPercentual)
    return f'Total do valor após aumento {resultado}, quantidade de aumento {qtdAumento}'

aux = aumento(2500,35)
print(aux)


"""
4 - Fizz Buzz - Se o parâmetro da função for divisível por 3, retorne fizz,
se o parâmetro da função for divisível por 5, retorne buzz. Se o parâmetro da
função for divisível por 5 e por 3, retorne FizzBuzz, caso contrário, retorne o
número enviado.
"""
def div(num):
    if num>0:
        if num%3 == 0 or num%5 == 0:
            if num%3==0 and num%5==0:
                return 'FizzBuzz'
            if num%3 == 0:
                return 'fizz'
            if num%5 == 0:
                return 'buzz'
        else:
            return f'{num}'
    else:
        return 'Valor inválido'

resultado = div(5)
resultado1 = div(3)
resultado2 = div(15)
resultado3 = div(2)
print(resultado)
print(resultado1)
print(resultado2)
print(resultado3)


from random import randint

for i in range(100):
    aleatorio = randint(0, 100)
    aux2 = div(aleatorio)
    print(f'Resultado de um número random = {aux2}')



"""
5 - Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor da
função2 executada.
"""

def func1(args):
    print(args)

def func2():
    var = 'Lucas Araujo'
    return var

func1(func2())


"""
6 - Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor da
função2 executada. Faça a função1 executar duas funções que recebam um número 
diferente de argumentos.
"""

def mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)


def fala_oi(nome):
    return f'Oi {nome}'


def saudacao(nome, saudacao):
    return f'{saudacao} {nome}'


executando = mestre(fala_oi, 'Luiz')
executando2 = mestre(saudacao, 'Luiz', saudacao='Bom dia!')
print(executando)
print(executando2)

