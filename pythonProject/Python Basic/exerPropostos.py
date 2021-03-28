"""
Faça um programa que peça ao usuário para digitar um número inteiro, informe se este número é par ou ímpar.
Caso o usuário não digite um número inteiro, informe que não é um número inteiro
"""

numInteiro = input('Digite um número inteiro: ')

try:
    numInteiro = int(numInteiro)
    if numInteiro%2 == 0:
        print(f'O número {numInteiro} é par')
    else:
        print(f'O número {numInteiro} é ímpar')
except:
    print(f'{numInteiro} não é um número inteiro')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito, exiba a saudação apropriada
EX.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23
"""
hora = input("que horas são? ")

try:
    hora = int(hora)
    if hora>=0 and hora<=11:
        print('Bom dia')
    elif hora<=17:
        print('Boa tarde')
    else:
        print('Boa noite')
except:
    print('Hora inválida!')


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos escreva
"Seu nome é curto"; se tiver entre 5 e 6 letras, escreva "seu nome é normal";
 maior que 6 escreva "Seu nome é muito grande.
"""

nome = input('digite seu nome: ')

try:
    if len(nome)<=4:
        print(f'{nome} seu nome é curto')
    elif len(nome)<=6:
        print(f'{nome} seu nome é normal')
    else:
        print(f'{nome} seu nome é muito grande')
except:
    print(f'{nome} inválido!')