# -*- coding: utf-8 -*-
#var = 1 #inteira
#va1 = 1.1 #float
#var3 = "String" #String
#var4 = true #boolean


#em python and = && e or == ||

#Comandos condicionais
x=2
y=3
if x>y:
    print("X>Y")
if y>x:
    print("Y>X")
elif x<3:
    print("é isso ai")
else:
    print("Y não é maior que X")

#Laços de repetição
g=0
while g<=10:
    print(g)
    g = g+1

lista = [1,2,3]
lista2 = ["lucas","maria","lorenzo"]

for i in lista2:
    print(i)

for i in range(10,20,2):
    print(i)

#comando input igual o Scanner do Java ou o scanf do C ou o cout do C++

numero = input("Digite um valor: ")
print("Seu número é: "+numero)

#Contar caracteres
casa = "casinha"
tamanho = len(casa)
print(tamanho)

print(casa[0])
print(casa[1])
print(casa[2])
print(casa[0:4])
#minusculo
print(casa.lower())
#maisculo
print(casa.upper())
#Strip remove espaços e caracteres especiais
conte = casa + " Isso" + "/n"
print(conte.strip())
#split
minha_string = "Lucas Edson Silva De Araújo"
minha_Lista = minha_string.split(" ")
print(minha_Lista)
#find
busca = minha_string.find("Silva")
print(busca)
print(minha_string[busca:])
#replace
minha_string = minha_string.replace("Silva","Nunes")
print(minha_string)
