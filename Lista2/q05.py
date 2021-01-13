# -*- coding: utf-8 -*-
#Escreva um programa que leia um arquivo multi-fasta e armazene em um dicionário:
#cabeçalho da sequência como a chave e a sequência como valor.
arquivo = open("seq.fasta")

linhas = arquivo.readlines()
multifasta = {}

for linha in linhas:
    if linha[0] == ">":
        seq_atual = linha[1:].strip()
        multifasta[seq_atual] = ""
    else:
        multifasta[seq_atual] = multifasta[seq_atual]+linha.strip()

print multifasta["seq3"]
