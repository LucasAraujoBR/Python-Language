import csv
import os
from datetime import datetime
import time
import copy

def pad(string):
    global name
    name = string
    

#Apenas limpa o CSV
def clearCsv():
    g = open("dadosCheios.csv", "r+")
    g.truncate(0)
    g.close() 

#Renomeia csv e envia para o diretório escolhido na função
def split(filehandler, delimiter=',', row_limit=10, 
    output_name_template='%s.csv', output_path='.', keep_headers=True):
    data = datetime.now()
    time.sleep(4)
    data = data.strftime('%d-%m-%Y  H-%H M-%M S-%S')
    output_name_template=name+' '+data+'%s.csv'   #parte_%s
    output_path = 'ArquivosCSV'
    #leitura do CSV
    reader = csv.reader(filehandler, delimiter=delimiter)
    #Lógica do contador para criação do nome do novo arquivo 
    #caso queira colocar em uma pasta especifíca, output_path = nome da pasta
    current_piece = ' TPF engenharia'
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

#Conta linhas do csv
def rows():
    with open('dadosCheios.csv','r') as csv_file:
        csv_reader = csv.reader(csv_file)
        row_count = sum(1 for row in csv_reader)  
        return row_count 

#Ecreve as listas no csv com limite de 10 linhas atuais
def escreveCsv(qtdSol,dadosRobo,tipoSolicitacao):
    listaProntaCsv = adaptaLista(dadosRobo) 
    pad(tipoSolicitacao)
    time.sleep(2)
    if(rows()==0):
        criaCab()
    if qtdSol<=10:                                      
        with open('dadosCheios.csv','a',newline='') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',')
            csv_writer.writerow(listaProntaCsv)
            csv_file.close()
        if (qtdSol==1):
            #criaCab()
            split(open('dadosCheios.csv','r'))
            clearCsv()
    else:
        with open('dadosCheios.csv','a',newline='') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',')
            csv_writer.writerow(listaProntaCsv)
            csv_file.close()
        if (rows()==10 or qtdSol==11):
            #criaCab()
            split(open('dadosCheios.csv','r'))
            clearCsv()

#Cria o cabeçalho padrão para cada arquivo gerado
def criaCab():
    lista = ['TIPO','ID','CNPJ/CPF','RAZÃO SOCIAL','FORMA DE PAGAMENTO ','BANCO','AGENCIA','CONTA','TIPO DE CONTA','NATUREZA DA CONTA',
'VALOR','VALOR PAGO','DATA SOLICITADA PARA PAGAMENTO','DATA DA SOLICITAÇÃO ','DATA DE PAGAMENTO','COMENTÁRIO ROBO','AJUSTE','STATUS SGP','DATA DE EXECUÇÃO ROBO','PRODUTO CONTÁBIL','DATA DE EMISSÃO','TIPO DO DOCUMENTO','NUMERO DE NOTA FISCAL','NATUREZA CONTÁBIL','CENTRO DE CUSTO','DATA EFETIVA DE VENCIMENTO','RATEIO','CONDIÇÃO DE PAGAMENTO',
'DATA DE LANCAMENTO NO TOTVS','MÓDULO','COLABORADOR SGP','COLABORADOR TOTVS','COMENTÁRIO FINANCEIRO','STATUS FINANCEIRO','DATA EFETIVA DE PAGAMENTO']
    with open('dadosCheios.csv','a',newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames = lista)
            writer.writeheader()
            csv_file.close()

#Renomeia indices da lista do robo que não serão passados 
def adaptaLista(lista):
    listaCop = copy.deepcopy(lista)
    # cont = 0
    # for i in lista:
    #     print(i,cont)
    #     cont+=1
    #Caso a lista não venha com todos os indices, for x in range(9)append(',')
    listaCop[11] = ' '
    listaCop[16] = ' '
    for x in range(18):
        listaCop.append(' ')
    listaCop
    return listaCop


dadosRobo = ['TIPO','ID','CNPJ/CPF','RAZÃO SOCIAL','FORMA DE PAGAMENTO ','BANCO','AGENCIA','CONTA','TIPO DE CONTA','NATUREZA DA CONTA',
'VALOR','VALOR PAGO','DATA SOLICITADA PARA PAGAMENTO','DATA DA SOLICITAÇÃO ','DATA DE PAGAMENTO','COMENTÁRIO ROBO','AJUSTE','STATUS SGP','DATA DE EXECUÇÃO ROBO']

print(dadosRobo)


# def retornaAux(qtdSol);
#     aux = qtdSol
#     return aux

#Invoca a lógica!




    #Tratamento da lista e retorno de lista copiada

aux =  15       #Simula quantidade de solicitações geradas pelo robo

for x in range(aux):
    escreveCsv(aux,dadosRobo,'PA')
    aux -=1


# qtd 
# aux = qtd
# Loop

# pad('PA')       #Nomear o setor, PA = Pagamento avulso. 
# time.sleep(3)
# escreveCsv(aux,listaProntaCsv)
#     aux -=1