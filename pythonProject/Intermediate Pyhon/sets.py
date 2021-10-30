# add (adiciona), update (atualiza), clear, discard
# union | (une)
# intersection & (todos os elementos presentes nos dois sets)
# difference - (elementos apenas no set da esquerda)
# symmetric_difference ^ (elementos que estão nos dois sets, mas não em ambos)

s1 = {1,2,3,4,5}
print(s1)

s2 = set()
s2.add(1)
s2.add(2)
s2.add((1,2,3,'Lucas'))
print(s2)
s2.discard((1,2,3,'Lucas'))
print(s2)
s3 = set()
s3.update('Python')
print(s3)

#eliminar elementos duplicados de uma lista
l1 = [1,2,11,3,4,5,6,6,6,6,6,6]
print(l1)
l1 = set(l1)    #remove duplicados
print(l1)
l1 = list(l1)   #transforma em lista novamente, agora sem os duplicados
print(l1)


#União

a1 = {1,2,3,4,5}
a2 = {1,2,3,4,5,6}
a3 = a1 | a2

print(a3) 

"""
-> É uma lista de listas de números inteiros
-> As listas internas tem o tamanho de 10 elementos
-> As listas internas contém números entre 1 a 10 e eles podem ser duplicados
Exercício
-> Crie uma função que encontra o primeiro duplicado considerando o segundo
    número como a duplicação. Retorne a duplicação considerada.
        Requisitos:
            A ordem do número duplicado é considerada a partir da segunda
            ocorrência do número, ou seja, o número duplicado em si.
            Exemplo:
                [1, 2, 3, ->3<-, 2, 1] -> 1, 2 e 3 são duplicados (retorne 3)
                [1, 2, 3, 4, 5, 6] -> Retorne -1 (não tem duplicados)
            Se não encontrar duplicados na lista, retorne -1
"""
lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]


#Solução 
def encontra_primeiro_duplicado(param_lista_de_inteiros):
    numeros_checados = set()
    primeiro_duplicado = -1

    for numero in param_lista_de_inteiros:
        if numero in numeros_checados:
            primeiro_duplicado = numero
            break

        numeros_checados.add(numero)

    return primeiro_duplicado


for lista_de_inteiros in lista_de_listas_de_inteiros:
    print(lista_de_inteiros, encontra_primeiro_duplicado(lista_de_inteiros))

"""
Os resultados devem ser:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10] -1
[9, 1, 8, 9, 9, 7, 2, 1, 6, 8] 9
[1, 3, 2, 2, 8, 6, 5, 9, 6, 7] 2
[3, 8, 2, 8, 6, 7, 7, 3, 1, 9] 8
[4, 8, 8, 8, 5, 1, 10, 3, 1, 7] 8
[1, 3, 7, 2, 2, 1, 5, 1, 9, 9] 2
[10, 2, 2, 1, 3, 5, 10, 5, 10, 1] 2
[1, 6, 1, 5, 1, 1, 1, 4, 7, 3] 1
[1, 3, 7, 1, 10, 5, 9, 2, 5, 7] 1
[4, 7, 6, 5, 2, 9, 2, 1, 2, 1] 2
[5, 3, 1, 8, 5, 7, 1, 8, 8, 7] 5
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1] -1
"""