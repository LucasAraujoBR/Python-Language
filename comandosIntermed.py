#append adiciona a lista minha_lista.append("Lucas")
# in saber se tem na lista
#del remove da lista del minha_lista[0:]
#sort faz ordenação da lista minha_lista.sort() caso queria decrecente minha_lista.sort(reverse=True)
#sorted retorna uma lista ja ordenada listaOrdaenada = sorted(minha_lista)
#reverse reverte a lista minha_lista.reverse()

#dicionario
meuDicionario = {"A":"Amora","B":"Bolacha","C":"Cuscuz"}
print(meuDicionario["B"]) #meuDicionario impreme com a chamada da chave !

for chave in meuDicionario:
    print(chave+"-"+meuDicionario[chave])  #imperime as chaves A,B e C
#items() retorna os valores separados ex ('A','Amora')
#values() retorna os valores da chave no caso Amora \n Bolacha \n Cuscuz
#read() lê arquivo inteiro
#readline() lê uma linha
#readline Lê arquivo e o armazena em uma lista
#Funções
def soma(x,y):
    print("A soma de ",x," + ",y," = " ,x+y)
soma(10,20)

def sub(x,y):
    return x-y
sub = sub(10,5)
print(sub)
#NUmeros random em python só pesquisar
#try:
# print(2/0)
#   except:
#       print("nãoeh permitida div por 0")
