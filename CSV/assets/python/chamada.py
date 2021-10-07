import funcoes as f
import chamadaPronta as c

#Clear para iniciar
f.clearCsv()

#caso a lista do robo só retorne um valor, usar apendList para adicionar a uma lista copiada e seguir na lógica atual.
totalDados = 15 #total de dados da lista do robo
#logica de lista teste
qtdTotal = totalDados+1  #Var total de linhas com +1 cabeçalho
print(qtdTotal)
headers = ['Duas Rodas','Uma Roda','Maritimo','Manual'] #Cabeçalho
f.escreveCsvCompleto(headers,qtdTotal)
erroProposital = []
listaPadrao = ['Carro','Moto','Barco','Bicicleta']  #Lista do robo
listaCopiada = f.checaLista(listaPadrao)                          #Copia da lista do robo, usando uma função de checagem
print(f.restoCsv(qtdTotal))

#Invoca chamadaPronta    (teste 5 dados)        OK!
# c.escreveCsvCompleto(listaCopiada,qtdTotal)
# c.escreveCsvCompleto(listaCopiada,qtdTotal)
# c.escreveCsvCompleto(listaCopiada,qtdTotal)
# c.escreveCsvCompleto(listaCopiada,qtdTotal)
# c.escreveCsvCompleto(listaCopiada,qtdTotal)


#Invoca chamadaPronta    (teste 15 dados)       OK!
c.escreveCsvCompleto(listaCopiada,qtdTotal)
c.escreveCsvCompleto(listaCopiada,qtdTotal)
c.escreveCsvCompleto(listaCopiada,qtdTotal)
c.escreveCsvCompleto(listaCopiada,qtdTotal)
c.escreveCsvCompleto(listaCopiada,qtdTotal)
c.escreveCsvCompleto(listaCopiada,qtdTotal)
c.escreveCsvCompleto(listaCopiada,qtdTotal)
c.escreveCsvCompleto(listaCopiada,qtdTotal)
c.escreveCsvCompleto(listaCopiada,qtdTotal)
c.escreveCsvCompleto(listaCopiada,qtdTotal)
c.escreveCsvCompleto(listaCopiada,qtdTotal)
c.escreveCsvCompleto(listaCopiada,qtdTotal)
c.escreveCsvCompleto(listaCopiada,qtdTotal)
c.escreveCsvCompleto(listaCopiada,qtdTotal)
c.escreveCsvCompleto(listaCopiada,qtdTotal)




#Chamada da lógica alternativa              (teste 5 dados) OK!
# f.escreveCsvAlternativo(listaCopiada,qtdTotal)
# f.escreveCsvAlternativo(listaCopiada,qtdTotal)
# f.escreveCsvAlternativo(listaCopiada,qtdTotal)
# f.escreveCsvAlternativo(listaCopiada,qtdTotal)
# f.escreveCsvAlternativo(listaCopiada,qtdTotal)
# if(f.rows()>0):
#     f.escreveRestoAlternativo()

#Chamada da lógica alternativa              (teste 22 dados)
# f.escreveCsvAlternativo(listaCopiada,qtdTotal)
# f.escreveCsvAlternativo(listaCopiada,qtdTotal)
# f.escreveCsvAlternativo(listaCopiada,qtdTotal)
# f.escreveCsvAlternativo(listaCopiada,qtdTotal)
# f.escreveCsvAlternativo(listaCopiada,qtdTotal)
# f.escreveCsvAlternativo(listaCopiada,qtdTotal)
# f.escreveCsvAlternativo(listaCopiada,qtdTotal)
# f.escreveCsvAlternativo(listaCopiada,qtdTotal)
# f.escreveCsvAlternativo(listaCopiada,qtdTotal)
# f.escreveCsvAlternativo(listaCopiada,qtdTotal)
# f.escreveCsvAlternativo(listaCopiada,qtdTotal)
# f.escreveCsvAlternativo(listaCopiada,qtdTotal)
# f.escreveCsvAlternativo(listaCopiada,qtdTotal)
# f.escreveCsvAlternativo(listaCopiada,qtdTotal)
# f.escreveCsvAlternativo(listaCopiada,qtdTotal)
# f.escreveCsvAlternativo(listaCopiada,qtdTotal)
# f.escreveCsvAlternativo(listaCopiada,qtdTotal)
# f.escreveCsvAlternativo(listaCopiada,qtdTotal)
# f.escreveCsvAlternativo(listaCopiada,qtdTotal)
# f.escreveCsvAlternativo(listaCopiada,qtdTotal)
# f.escreveCsvAlternativo(listaCopiada,qtdTotal)
# f.escreveCsvAlternativo(listaCopiada,qtdTotal)
# f.escreveCsvAlternativo(listaCopiada,qtdTotal)
# f.escreveCsvAlternativo(listaCopiada,qtdTotal)
# f.escreveCsvAlternativo(listaCopiada,qtdTotal)
# f.escreveCsvAlternativo(listaCopiada,qtdTotal)
# if(f.rows()>0):
#     f.escreveRestoAlternativo()





# f.escreveCsvCompleto(listaCopiada,qtdTotal)
# f.escreveCsvCompleto(listaCopiada,qtdTotal)
# f.escreveCsvCompleto(listaCopiada,qtdTotal)
# f.escreveCsvCompleto(listaCopiada,qtdTotal)
# f.escreveCsvCompleto(listaCopiada,qtdTotal)
# f.escreveCsvCompleto(listaCopiada,qtdTotal)
# f.escreveCsvCompleto(listaCopiada,qtdTotal)
# f.escreveCsvCompleto(listaCopiada,qtdTotal)
# f.escreveCsvCompleto(listaCopiada,qtdTotal)
# f.escreveCsvCompleto(listaCopiada,qtdTotal)
# f.escreveCsvCompleto(listaCopiada,qtdTotal)
# f.escreveCsvCompleto(listaCopiada,qtdTotal)
# f.escreveCsvCompleto(listaCopiada,qtdTotal)
# f.escreveCsvCompleto(listaCopiada,qtdTotal)
# f.escreveCsvCompleto(listaCopiada,qtdTotal)
