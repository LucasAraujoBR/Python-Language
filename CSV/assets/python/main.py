import pandas as pd
import csv


#Leitura dos dados
excelFile = pd.read_excel(r"C:\Users\Lucas Araújo\Documents\Pasta config git\CSVfiles\ExcelFiles\ex.xlsx", sheet_name="Planilha1")


# 1. cria o arquivo
f = open('primeira.csv', 'w', newline='', encoding='utf-8')
f2 = open('segunda.csv', 'w', newline='', encoding='utf-8')

# 2. cria o objeto de gravação
w = csv.writer(f)
y = csv.writer(f2)

#Extraindo 10 dados da primeira coluna  e inserindo num csv
for i in range(12):
    dados = excelFile.select_dtypes(include='number').head(i)
    w.writerow([dados])

#Extraindo 10 dados da segunda coluna  e inserindo num csv
for i in range(12):
    dados = excelFile.select_dtypes(include='object').head(i)
    y.writerow([dados])

#fechando csv
f.close() 
f2.close()
