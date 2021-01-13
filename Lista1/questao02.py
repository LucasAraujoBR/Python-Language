# -*- coding: utf-8 -*-
#Faça um programa que receba duas notas digitadas pelo usuário.
# Se a nota for maior ou igual a seis, escreva aprovado, senão escreva reprovado.

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = float((nota1+nota2)/2)

if media<6:
    print("Reprovado com média: ",media)
else:
    print("Aprovado com média: ",media)
