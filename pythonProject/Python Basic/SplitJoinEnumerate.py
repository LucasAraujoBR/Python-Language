"""
Aula 20 - Split, Join e Enumerate
* Split - dividir uma string # str
* Join - juntar uma lista # str
* Enumerate - Enumerar elementos da lista # list
* Desenpacotamento de listas
* Invertendo valores entre duas variaveis
"""
String = 'Eu sou país do futebol, tocou Neymar é gol é gol é'
lista = String.split(' ')
lista1 = String.split(',')

print(lista)
print(lista1)


for valor in lista:
    print(f'A palavra "{valor}" apareceu {lista.count(valor)}x vezes na frase.')

#Função strip() remove espaços

print('---------------------------------------------------------------------------------------------------')
palavra = ''
cont = 0
for valor in lista:
    qnd_vezes = lista.count(valor)
    if qnd_vezes > cont:
        cont = qnd_vezes
        palavra = valor

print(f'A palavra que mais apareceu foi "{palavra}" ({cont}X)')

print()
print('-----------------------------------------------JOIN--------------------------------------------------------')
print()


texto = 'Python aprendizado básico no começo de 2021'
list = texto.split(' ')
texto2 = '|'.join(list)
print(list)
print(texto2)

print()
print('-----------------------------------------ENUMERATE-----------------------------------------------------------')
print()


string = 'O show começou em 2020'
kist = string.split(' ')

for cont,valor in enumerate(kist):
    print(cont,valor, kist[cont])

"""
Desenpacotamento de listas 
"""

listando = ['a','b','c',1,2,3,4]
#n1,n2,n3 = listando
n1,n2,*outro, ultimoValorDaLista = listando         #Ponto *qualquer valor tira o erro do desenpacotamento
print(outro)    #Cria outra lista com o resto da lista mãe
print(n1)
print(n2)
print(ultimoValorDaLista)   #Pega o ultimo valor da lista

"""
Invertendo valores entre duas variaveis  
"""

x = 'lucas'
y = 10

x, y =y, x
print(f'X={x} Y={y}')

z = 'edson'
w = 10
q = 'que'

z,w,q = q,z,w   #Nova ordem
print(f'Z = {z} Q = {q} W = {w}')