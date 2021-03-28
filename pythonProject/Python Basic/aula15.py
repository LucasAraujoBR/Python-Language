"""
Aula 15 - Manipulção de Strings
* String indices
* Fatiamento de strings [inicio:fim:passo]
* Funções built-in len, abs, type, print, etc...
Essas funções podem ser usadas diretamente em cada tipo.
Você pode conferir tudo isso em:
https://docs.python.org/3/library/stdtypes.html (tipos built-in)
https://docs.python.org/3/library/functions.html (Funções built-in)
"""

texto = 'textando123'
print(texto[2]) #Indice 2 = x
print(texto[-1])
print(texto[-4])
url = 'www.google.com.br/'
print(url[:-1])

novaString = texto[2:6]
novaString2 = texto[:6]
novaString3 = texto[0:6:2]
print(novaString)
print(novaString2)
print(novaString3)

for letra in texto:
    print(letra)