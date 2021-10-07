# -*- coding: cp1252 -*-
import pandas as pd
import csv

localExcel = 'aumento.xlsx'
#Lê o arquivo Excel       
df = pd.read_excel(localExcel)

localArquivoCsv = 'arquivoModificado.csv'
#passa auterações para um csv(Indicando diretórios)
df.to_csv(localArquivoCsv)




   