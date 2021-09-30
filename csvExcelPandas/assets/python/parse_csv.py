# -*- coding: cp1252 -*-
import csv 
from datetime import datetime
import pandas as pd

#%H:%M:%S:%M
data = datetime.now()
data = data.strftime('%d-%m-%Y-H%H-M%M-S%S')
print(data)

#Passando strings formatadas para usar nas funções 
Tabela1 = data+'parte1.csv'
Tabela2 = data+'parte2.csv'
Tabela3 = data+'parte3.csv'
Tabela4 = data+'parte4.csv'
TabelaModificada = 'arquivoModificado.csv'


#Printa a tabela de dados mãe
def printStatus(a):
    with open(a,'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            print(line)

#Cria nova tabela recebendo nomes como parametros 
def createNewCsv(a,b,c,d,e):
    with open(a,'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        with open(b,'w') as new_file:
            with open(c,'w') as new_file2:
                with open(d,'w') as new_file3:
                    with open(e,'w') as new_file4:
                        cont = 0
                        csv_writer1 = csv.writer(new_file, delimiter='\t')
                        csv_writer2 = csv.writer(new_file2, delimiter='\t')
                        csv_writer3 = csv.writer(new_file3, delimiter='\t')
                        csv_writer4 = csv.writer(new_file4, delimiter='\t')
                        for line in csv_reader:
                            if(cont<10):
                                cont+=1
                                csv_writer1.writerow(line)      
                            elif(cont<20):
                                cont+=1
                                csv_writer2.writerow(line)
                            elif(cont<30):
                                cont+=1
                                csv_writer3.writerow(line) 
                            elif(cont<40):
                                cont+=1
                                csv_writer4.writerow(line)  
                            else: 
                                break          
#Conta linhas da tabela mãe
def Rows(a):
    with open(a,'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        row_count = sum(1 for row in csv_reader)  
        return row_count

cf = pd.read_csv(TabelaModificada, encoding="UTF-8")
#Chamando funções
printStatus(TabelaModificada)
totalLinhas = Rows(TabelaModificada)
createNewCsv(TabelaModificada,Tabela1,Tabela2,Tabela3,Tabela4)

