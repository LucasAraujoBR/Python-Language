import os
from datetime import datetime
import csv
import pandas as pd





#Apenas limpa o CSV
def clearCsv():
    g = open("dadosCheios.csv", "r+")
    g.truncate(0)
    g.close() 


#Escreve no csv
def escreveCsv(lista,qtdTotal):
    with open('dadosCheios.csv','a',newline='') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',')
            csv_writer.writerow(lista)
            csv_file.close()
            qtdCsv = restoCsv(qtdTotal)
            if(qtdTotal>11 and 11 == rows()):   #OK!
                split(open('dadosCheios.csv', 'r'))
                clearCsv()
                print('Cheio!')
            elif(qtdTotal<11 and qtdTotal == rows()):
                split(open('dadosCheios.csv', 'r')) #OK!
                clearCsv()
                print('menor Quantidade Adicionada!')
            else:
                return print('Rodando...')


def escreveResto(qtdTotal):
    qtdCsv = (restoCsv(qtdTotal)-1)
    print(rows())
    print(qtdCsv)
    if(rows() == qtdCsv):
        split(open('dadosCheios.csv', 'r')) #??
        clearCsv()
        print('Adicionado')

########################################################Lógica preferida#######################
# Funcionando ao armazenar todos os dados num csv só
def escreveCsvCompleto(lista,qtdTotal):
    with open('dadosCheios.csv','a',newline='') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',')
            csv_writer.writerow(lista)
            csv_file.close()
            if(qtdTotal == rows()):
                split(open('dadosCheios.csv', 'r'))
                clearCsv()
###############################################################################################

############################################################################################
#Lógica alternativa de escrita csv
def escreveCsvAlternativo(lista,qtdTotal):
    with open('dadosCheios.csv','a',newline='') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',')
            csv_writer.writerow(lista)
            csv_file.close()
            if(11 == rows()):
                split(open('dadosCheios.csv', 'r'))
                clearCsv()
                print('Cheio!')
            elif(qtdTotal<11 and rows() == qtdTotal):
                split(open('dadosCheios.csv', 'r'))
                clearCsv()

def escreveRestoAlternativo():
    splitResto(open('dadosCheios.csv', 'r')) #??
    clearCsv()
    print('Adicionado')
###############################################################################################

#Conta linhas do csv
def rows():
    with open('dadosCheios.csv','r') as csv_file:
        csv_reader = csv.reader(csv_file)
        row_count = sum(1 for row in csv_reader)  
        return row_count 


#Função que retorna o resto para completar o csv
def restoCsv(qtdTotal):
    a = qtdTotal % 10
    return a

def retornaPar():
    a = rows()+1
    return a
# def contador(cont,qtdTotal):
#     a = qtdTotal % 10
#     a = int(a)
#     if(cont == a):
#         return True
#     else:
#         cont += 1
    
    


#Separa o csv e envia para um diretório com nome formatado
def split(filehandler, delimiter=',', row_limit=10, 
    output_name_template='parte_%s.csv', output_path='.', keep_headers=True):
    data = datetime.now()
    data = data.strftime('%d-%m-%Y  H-%H M-%M S-%S')
    output_name_template=data+'parte_%s.csv'
    output_path = 'ArquivosCSV'
    #leitura do CSV
    reader = csv.reader(filehandler, delimiter=delimiter)
    #Lógica do contador para criação do nome do novo arquivo 
    #caso queira colocar em uma pasta especifíca, output_path = nome da pasta
    current_piece = 1
    current_out_path = os.path.join(
        output_path,
        output_name_template  % current_piece
    )
    #escreve no novo arquivo
    current_out_writer = csv.writer(open(current_out_path, 'w',newline=''), delimiter=delimiter)
    current_limit = row_limit
    if keep_headers:
        headers = next(reader)
        current_out_writer.writerow(headers)
    for i, row in enumerate(reader):
        if i + 1 > current_limit:
            current_piece += 1
            current_limit = row_limit * current_piece
            current_out_path = os.path.join(
            output_path,
            output_name_template  % current_piece
            )
            current_out_writer = csv.writer(open(current_out_path, 'w',newline=''), delimiter=delimiter)
            if keep_headers:
                current_out_writer.writerow(headers)
        current_out_writer.writerow(row)

#Separa o csv e envia para um diretório com nome formatado
def splitResto(filehandler, delimiter=',', row_limit=10, 
    output_name_template='resto_%s.csv', output_path='.', keep_headers=True):
    data = datetime.now()
    data = data.strftime('%d-%m-%Y  H-%H M-%M S-%S')
    output_name_template=data+'resto_%s.csv'
    output_path = 'ArquivosCSV'
    #leitura do CSV
    reader = csv.reader(filehandler, delimiter=delimiter)
    #Lógica do contador para criação do nome do novo arquivo 
    #caso queira colocar em uma pasta especifíca, output_path = nome da pasta
    current_piece = 1
    current_out_path = os.path.join(
        output_path,
        output_name_template  % current_piece
    )
    #escreve no novo arquivo
    current_out_writer = csv.writer(open(current_out_path, 'w',newline=''), delimiter=delimiter)
    current_limit = row_limit
    if keep_headers:
        headers = next(reader)
        current_out_writer.writerow(headers)
    for i, row in enumerate(reader):
        if i + 1 > current_limit:
            current_piece += 1
            current_limit = row_limit * current_piece
            current_out_path = os.path.join(
            output_path,
            output_name_template  % current_piece
            )
            current_out_writer = csv.writer(open(current_out_path, 'w',newline=''), delimiter=delimiter)
            if keep_headers:
                current_out_writer.writerow(headers)
        current_out_writer.writerow(row)


def checaLista(lista):
    erroPadrao = ['Erro','Erro','Erro','Erro',]
    if(len(lista) > 0):
        return lista
    else:
        return erroPadrao