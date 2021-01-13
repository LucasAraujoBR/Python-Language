# -*- coding: utf-8 -*-
#Escreva um programa que compare se duas sequências digitadas pelo usuário são iguais.
import re

seq1 = "AT.GA.*"
seq2 = "ATTGAAAAAA"

buscar = re.match(seq1,seq2)

if buscar:
    print ("sequências identicas")
    print (buscar.group())
else:
    print ("sequências diferentes")
