"""
Função anonima 
"""
a = lambda x, y: x*y    #Dessa forma pode chamar a função sem dar um nome a mesma, sem usar return
print(a(5,5))   

#Ordenando listas

lista = [
    ['P1' , 5],
    ['P2' , 35],
    ['P5' , 21],
    ['P4' , 50],
    ['P3' , 4],
]
#Ordenando lista pelo preço
def func(item): 
    return item[1]
lista.sort(key=func)
print(lista)
#Ordenando pelo nome
def func2(item): 
    return item[0]
lista.sort(key=func2)
print(lista)

#Ordenando com lambda
lista.sort(key=lambda item: item[1])    #Ordenando em relação ao preço
print(lista)
lista.sort(key=lambda item: item[0] )   #Ordenando em relação ao nome
print(lista)

#Ordenando sem mudar a lista original
print(sorted(lista,key=lambda aux: aux[1])) #Ordenando em relação ao preço
print(sorted(lista,key=lambda aux: aux[0])) #Ordenando em relação ao nome