import os
from datetime import datetime
import csv
import pandas as pd
import testes

#Salva csv
# def saveCsv(a):
#     data = datetime.now()
#     data = data.strftime('%d-%m-%Y  H-%H M-%M S-%S')
#     df = pd.read_csv("dadosCheios.csv")
#     df.to_csv('ArquivosCSV/'+data+'part'+str(a)+'.csv')


#Apenas limpa o CSV
def clearCsv():
    f = open("dadosCheios.csv", "r+")
    f.truncate(0)
    f.close() 

#Escreve no csv
def escreveCsv(lista,qtdTotal):
    with open('dadosCheios.csv','a',newline='') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',')
            csv_writer.writerow(lista)
            csv_file.close()
            if(qtdTotal == rows()):
                testes.split(open('dadosCheios.csv', 'r'))
                clearCsv()

#             limitadorLinhas(qtdTotal)
 #Conta linhas do csv
def rows():
    with open('dadosCheios.csv','r') as csv_file:
        csv_reader = csv.reader(csv_file)
        row_count = sum(1 for row in csv_reader)  
        return row_count 

        
# def limitadorLinhas(qtdTotal):
#     if(qtdTotal>10 and rows()==11): #OK!
#         saveCsv(2)
#         clearCsv()
#     if(qtdTotal<11 and qtdTotal == rows()):   #OK!
#         saveCsv(1)
#         clearCsv()
#     if(rows() < 10 and qtdTotal>10 and restoCsv(qtdTotal) == rows()):
#         saveCsv(3)
#         clearCsv()

#Função que retorna o resto para completar o csv
# def restoCsv(qtdTotal):
#     a = qtdTotal % 10
#     b = a - int(a)
#     total = b * 10
#     return total

#Clear para iniciar
clearCsv()

#caso a lista do robo só retorne um valor, usar apendList para adicionar a uma lista copiada e seguir na lógica atual.

#logica de lista teste
qtdTotal = 1+1
headers = ['Duas Rodas','Uma Roda','Maritimo','Manual']
escreveCsv(headers,qtdTotal)
listaPadrao = ['Carro','Moto','Barco','Bicicleta']
listaCopiada = listaPadrao
erroPadrao = ['Erro','Erro','Erro','Erro',]
print(listaCopiada)
if(len(listaCopiada) > 0):
    #Invoca função de escrita no csv
    escreveCsv(listaCopiada,qtdTotal)
else:
    escreveCsv(erroPadrao,qtdTotal)
    



