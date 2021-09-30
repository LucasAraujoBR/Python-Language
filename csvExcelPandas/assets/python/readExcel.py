# -*- coding: cp1252 -*-
import pandas as pd
import csv

localExcel = 'aumento.xlsx'
#Lê o arquivo Excel       
df = pd.read_excel(localExcel)

#Manipulando dados
valor = df['Valor']
status = df['status']
print(df)
df['Aumento'] = valor * 0.20
df['Total'] = valor + (valor * 0.20)
df['status'] = df['status'].str.replace('analise','ok')
print(df)

localNovoExcel = 'AumentosRealizados.xlsx'
#passa auterações para um excel(Indicando diretórios)
df.to_excel (localNovoExcel, index = False, header=True)

localArquivoCsv = 'arquivoModificado.csv'
#passa auterações para um csv(Indicando diretórios)
df.to_csv(localArquivoCsv)




   