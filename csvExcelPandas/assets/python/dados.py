import pandas as pd
import csv




#leitura do csv
df = pd.read_csv(r"C:\Users\Lucas Araújo\Documents\Pasta config git\CSVfiles\Financeiro.csv")

#Criação das colunas
#df['Valores'] = ''
#df['Status'] = ''
print(df.columns)
print(df.values)


def writeDates(dados):
    w.writerow([(dados)])


#leitura do excel
ef = pd.read_excel(r"C:\Users\Lucas Araújo\Documents\Pasta config git\CSVfiles\ExcelFiles\aumento.xlsx", sheet_name="func")

#abertura arquivo csv
f = open('Financeiro.csv', 'w', newline='', encoding='utf-8')


# 2. cria o objeto de gravação
w = csv.writer(f)

#Extraindo dados da primeira coluna
dados = ef.select_dtypes(include='number').head(5)

#inserindo no csv
df['Valores'] = w.writerow([(dados+150)])

#Extraindo dados da segunda coluna
status = ef.select_dtypes(include='object').head(5)

#alterando status
d = {'analise':'concluído'}
status = status.replace(d) 
df['Status'] = w.writerow([status])
    

#fechando csv
f.close() 


