import os
from datetime import datetime
import csv
import pandas as pd


#Conversão de Excel para CSV
localExcel = 'aumento.xlsx'
#Lê o arquivo Excel       
df = pd.read_excel(localExcel)

localArquivoCsv = 'arquivoModificado.csv'
#passa auterações para um csv(Indicando diretórios)
df.to_csv(localArquivoCsv)

"""
    Argumentos:
        row_limit: O número de linhas que você deseja em cada arquivo de saída. 10.000 por padrão.
        output_name_template: Um modelo no estilo% s para os arquivos de saída numerados.
        output_path: Onde colocar os arquivos de saída.
        keep_headers: Se deve ou não imprimir os cabeçalhos em cada arquivo de saída.

    Libs:
        os => usada para criação de objeto arquivo e diretório, no exemplo data+parte_contador.csv
        datetime => Apenas para retornar a data atual
        csv => para abertura, escrita e fechamento

    Exemplo de uso:
    split(open('meuArquivo.csv', 'r'))  
"""  
def split(filehandler, delimiter=',', row_limit=10, 
    output_name_template='parte_%s.csv', output_path='.', keep_headers=True,):
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





split(open('arquivoModificado.csv', 'r'))


