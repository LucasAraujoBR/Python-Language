"""
Jogo da forca em pyhton
"""

secreto = input("Digite a palavra secreta: ")
digitadas = []
chances = 15

while True:
    if chances <= 0:
        print('Você perdeu!!!')
        break

    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Ahhh isso não vale, digite apenas uma letra.')
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f'Acertoooou "{letra}" existe na palavra secreta.')
    else:
        print(f'Errou, a letra "{letra}" NÃO EXISTE na palavra secreta.')
        digitadas.pop()

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == secreto:
        print(f'VOCÊ GANHOU!!! A palavra era {secreto_temporario}.')
        break
    else:
        print(f'Jogo da Forca: {secreto_temporario}')

    if letra not in secreto:
        chances -= 1

    print(f'Você ainda tem {chances} tentativas.')
    print()
