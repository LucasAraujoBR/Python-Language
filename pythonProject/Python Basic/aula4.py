"""
Aula 4 Tipos de Dados
str - string 'fulano'
int - inteiro   123456
float - real/ponto flutuante    12.5
bool - booleano/lógico  1 or 0  (True or False)
"""
print(type("Lucas"))
print(type(123456))
print(type(10.5))
print(type(True))

print(bool(1==2))   #cast para booleando
print(type(int("10")))  #TypeCasting


'''
Atividade 
'''
#string nome
print("Lucas",type("Lucas"))
#int idade
age = 22
print(22,type(22))
#float altura
print(1.82,type(1.82))
#bool maior de idade
print(age>18,type(age>18))