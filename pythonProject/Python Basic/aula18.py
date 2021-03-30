"""
Aula 18 - Listas em python
fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
"""

lista = ['lucas', 1, 2, 2.2, True]
print(lista[0])
print(lista)
print(lista[0:3])
print(lista[2:])    # (Start=0:stop:step=1)
lista[0] = 'Edson'
print(lista[0])

l1 = [1,2,3]
l2 = [4,5,6]
l3 = l1 + l2
print(l1)
print(l2)
print(l1+l2)
l1.extend('a')
print(l1)
l1.extend(l2)   #sempre add no final da lista
print(l1)
l1.insert(0,"Inserido no indice 0") #add no indice escolhido  (indice,valor)
print(l1)
l1.pop()    #remove o ultimo valor da lista
print(l1)
del(l1[0:2])    #Remove os indices selecionados
print(l1)
l4 = [1,4,3]
print(max(l4))  #pega o maior valor da lista
print(min(l4))  #pega o menor valor da lista

l5 = list(range(0,100,1))
for valor in l5:
    print(valor)

