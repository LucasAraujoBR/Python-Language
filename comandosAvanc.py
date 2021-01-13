#list comprehension

x=[1,2,3,4,5]
y=[]

for i in x:
    y.append(i**2)

print(x)
print(y)
#ou
x=[1,2,3,4,5]
y=[i**2 for i in x]

print(x)
print(y)

#numeros impares
x=[1,2,3,4,5]
y=[i**2 for i in x]
z=[i for i in x i%2==1]

print(z)

#Função enumerate

lista = ["BOLA","CARRO","ZEBRA"]

for i, nome int enumerate(lista)
    print(i, nome)

#Função filter

def pares(i):
    if i%2 == 0:
        return i
def impares(i):
    if i%2 == 1
        return i
lista = [1,2,3,4,5,6,7,8,9,10]
lista_pares = filter(pares, lista)
lista_impares - filter(impares,lista)
print(list(lista_pares))
print(list(lista_impares))

#Função reduce
from functools import reduce

def soma(x,y):
    return x+y

lista = [1,3,5,10,20]

soma = reduce(soma, lista)
print(soma)

#Função zip

lista = [1,2,3,4,5]
lista2 = ["MAÇA","UVA","BOLA","CACHORRO","CARRO"]
lista3 = ["R$ 2,00","R$ 0,50","R$ 20,00","Não tem preço","R$ 50.000,00"]

for numero, nome, valor in zip(lista,lista2,lista3):
    print(numero, nome, valor)

#Função map
def dobro(x):
    return x*2
valor = [1,2,3,4,5]
valor_dobrado = map(dobro, valor)
valor_dobrado = list(valor_dobrado)
print(valor_dobrado)

#Funcão lambda obj criar uma fun que so sera usada uma unica vez
valor = [1,2,3,4,5]
valor_dobrado = map(lambda i:i*2, valor)
