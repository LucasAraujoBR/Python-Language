# -*- coding: utf-8 -*-
#Escreva um programa que exiba um menu e pergunte o que o usuário deseja fazer. Se o usuário digitar 1,
#o programa deve chamar uma função que lê um arquivo de texto. Se o usuário apertar 2,
#o programa deve imprimir o conteúdo do arquivo lido anteriormente. Se o usuário apertar três o programa deve ser fechado.
import glob

arquivos_pasta = glob.glob("*")
print(arquivos_pasta)
menu = 0
def abrirArquivo():
    nome = input("Digite o nome do arquivo que deseja abrir: ")
    arquivo = open(nome)
    return arquivo
def lerArquivo(arquivo):
    linhas = arquivo.readlines()
    for liha in linhas:
        print(linha.strip())

while menu != 3:
    print("(1) Abrir arquivo\n(2) Ler arquivo\n(3) Sair\n")
    menu = input("Digite a opção desejada: ")
    if menu == 1:
        arquivo = abrirArquivo()
    elif menu == 2:
        lerArquivo(arquivo)
