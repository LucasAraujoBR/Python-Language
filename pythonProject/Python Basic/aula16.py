"""
Aula 16 - While, estrutura de repetição em python
while = enquanto for verdadeira, repita!
"""
# x = 0
# while x<=10:
#     if x == 3:
#         x += 1
#         continue    #Pula essa etapa do laço
#     print(x)
#     x += 1
#
# print(f'Laço encerrado')
#
#
# w = 0
# z = 0
#
# while w<=10:
#     z = 0
#     while z<5:
#         print(f'{w} {z}')
#         z+=1
#     w+=1
#

"""
Calculadora apenas com While e if
"""
#
# while True:
#     try:
#         num = float(input('primeiro número: '))
#         num1 = float(input('segundo número: '))
#         operator = input('digite o perador (+, -, /, *): ')
#         close = input('deseja sair? [s] ou [n]: ')
#         if close == 's':
#             break
#         if operator == '+':
#             print(f'{num} {operator} {num1} = {num + num1}')
#         elif operator == '-':
#             print(f'{num} {operator} {num1} = {num - num1}')
#         elif operator == '/':
#             print(f'{num} {operator} {num1} = {num / num1}')
#         else:
#             print(f'{num} {operator} {num1} = {num * num1}')
#
#     except:
#         print('Dado inválidos!')



"""
Contadores
Acumuladores
"""

# cont = 1
# acumulator = 1
#
# while cont<10:
#     print(cont,acumulator)
#     acumulator = acumulator + cont
#     cont +=1
# else:                       #se eu usar um break dentro do laço o else não sera executado!
#     print('cheguei no else.')
#

"""
Iterando strings com while
"""
frase = 'o rato roeu a roupa do rei de roma'
tam_frase = len(frase)
cont = 0
novaStringMestre = ''
input_do_usuario = input('qual letra deseja tornar maiúscula? ')
while cont < tam_frase:
    # print(frase[cont],cont)
    # novaStringMestre += frase[cont]
    # letra = frase[cont]
    # if letra == 'r':
    #     novaStringMestre += 'R'
    # else:
    #     novaStringMestre += letra
    letra = frase[cont]
    if letra == input_do_usuario:
        novaStringMestre += input_do_usuario.upper()
    else:
        novaStringMestre += letra
    print(novaStringMestre)
    cont += 1

print(novaStringMestre)