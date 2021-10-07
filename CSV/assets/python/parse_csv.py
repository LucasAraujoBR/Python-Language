# -*- coding: cp1252 -*-
import csv 
from datetime import datetime
import pandas as pd

#%H:%M:%S:%M
data = datetime.now()
data = data.strftime('%d-%m-%Y  H-%H M-%M S-%S')
print(data)




#Printa a tabela de dados mãe
def printStatus(a):
    with open(a,'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            print(line)

#Cria nova tabela recebendo nomes como parametros 
def createNewCsv(a,b,aux):
    with open(a,'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        with open(b,'w') as new_file:
                        cont = 0
                        csv_writer = csv.writer(new_file, delimiter='\t')
                        for line in csv_reader:
                            if(aux == 1):
                                if(cont<10):
                                    cont+=1
                                    csv_writer.writerow(line)      
                                else: 
                                    break 
                            if(aux == 2):
                                if(cont<20):
                                    cont+=1
                                    if(cont > 10):
                                        csv_writer.writerow(line)      
                                else: 
                                    break   
                            if(aux == 3):
                                if(cont<30):
                                    cont+=1
                                    if(cont > 20):
                                        csv_writer.writerow(line)      
                                else: 
                                    break 
                            if(aux == 4):
                                if(cont<40):
                                    cont+=1
                                    if(cont > 30):
                                        csv_writer.writerow(line)      
                                else: 
                                    break   
                            if(aux == 5):
                                if(cont<50):
                                    cont+=1
                                    if(cont > 40):
                                        csv_writer.writerow(line)      
                                else: 
                                    break 
                            if(aux == 6):
                                if(cont<60):
                                    cont+=1
                                    if(cont > 50):
                                        csv_writer.writerow(line)      
                                else: 
                                    break 
                            if(aux == 7):
                                if(cont<70):
                                    cont+=1
                                    if(cont > 60):
                                        csv_writer.writerow(line)      
                                else: 
                                    break
                            if(aux == 8):
                                if(cont<80):
                                    cont+=1
                                    if(cont > 70):
                                        csv_writer.writerow(line)      
                                else: 
                                    break
                            if(aux == 9):
                                if(cont<90):
                                    cont+=1
                                    if(cont > 80):
                                        csv_writer.writerow(line)      
                                else: 
                                    break
                            if(aux == 10):
                                if(cont<100):
                                    cont+=1
                                    if(cont > 90):
                                        csv_writer.writerow(line)      
                                else: 
                                    break   




#Conta linhas da tabela mãe
def rows(a):
    with open(a,'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        row_count = sum(1 for row in csv_reader)  
        return row_count






#Chamando funções
data = datetime.now()
data = data.strftime('%d-%m-%Y  H-%H M-%M S-%S')


#teste66.csv teste92.csv arquivoModificado.csv
#Passando strings formatadas para usar nas funções 
TabelaModificada = 'arquivoModificado.csv'
#teste = 'teste.csv'
cf = pd.read_csv(TabelaModificada, encoding="UTF-8")

aux = 1
linhas = rows(TabelaModificada)
if(linhas < 10):
    for x in range (0,1):
        print(1)
        createNewCsv(TabelaModificada,data+' parte'+str(aux)+'.csv',aux)
elif(linhas < 20):
    for x in range (0,2):
        print(2)
        createNewCsv(TabelaModificada,data+' parte'+str(aux)+'.csv',aux) 
        aux = int(aux) + 1 
elif(linhas < 30):
    for x in range (0,3):
        print(3)
        createNewCsv(TabelaModificada,data+' parte'+str(aux)+'.csv',aux) 
        aux = int(aux) + 1
elif(linhas < 40):
    for x in range (0,4):
        print(4)
        createNewCsv(TabelaModificada,data+' parte'+str(aux)+'.csv',aux) 
        aux = int(aux) + 1
elif(linhas < 50):
    for x in range (0,5):
        print(5)
        createNewCsv(TabelaModificada,data+' parte'+str(aux)+'.csv',aux) 
        aux = int(aux) + 1              
elif(linhas < 60):
    for x in range (0,6):
        print(6)
        createNewCsv(TabelaModificada,data+' parte'+str(aux)+'.csv',aux) 
        aux = int(aux) + 1          
elif(linhas < 70):
    for x in range (0,7):
        print(7)
        createNewCsv(TabelaModificada,data+' parte'+str(aux)+'.csv',aux) 
        aux = int(aux) + 1  
elif(linhas < 80):
    for x in range (0,8):
        print(8)
        createNewCsv(TabelaModificada,data+' parte'+str(aux)+'.csv',aux) 
        aux = int(aux) + 1
elif(linhas < 90):
    for x in range (0,9):
        print(9)
        createNewCsv(TabelaModificada,data+' parte'+str(aux)+'.csv',aux) 
        aux = int(aux) + 1
elif(linhas < 100):
    for x in range (0,10):
        print(10)
        createNewCsv(TabelaModificada,data+' parte'+str(aux)+'.csv',aux) 
        aux = int(aux) + 1   
  
