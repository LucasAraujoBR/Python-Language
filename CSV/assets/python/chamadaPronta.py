import os
from datetime import datetime
import csv
import pandas as pd
import time

#Conta linhas do csv
def rows():
    with open('dadosCheios.csv','r') as csv_file:
        csv_reader = csv.reader(csv_file)
        row_count = sum(1 for row in csv_reader)  
        return row_count 


#Apenas limpa o CSV
def clearCsv():
    g = open("dadosCheios.csv", "r+")
    g.truncate(0)
    g.close() 

def checaLista(lista):
    erroPadrao = ['erro','erro','erro','erro']
    if(len(lista)>0):
        return lista
    else:
        return erroPadrao


# Funcionando ao armazenar todos os dados num csv só
def escreveCsvCompleto(lista,qtdTotal):
    with open('dadosCheios.csv','a',newline='') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',')
            csv_writer.writerow(lista)
            csv_file.close()
            if(qtdTotal == rows()):
                split(open('dadosCheios.csv', 'r'))
                clearCsv()

#Separa o csv e envia para um diretório com nome formatado
def split(filehandler, delimiter=',', row_limit=10, 
    output_name_template='parte_%s.csv', output_path='.', keep_headers=True):
    data = datetime.now()
    time.sleep(1000)
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