import os

perguntas = {
        'pergunta 1' : {
        'pergunta':'De quem é a famosa frase “Penso, logo existo”?',
        'respostas':{'a':'Platão','b':'Sócrates','c':'Descartes','d':'Francis Bacon',},
        'resposta_correta':'c',
    },
        'pergunta 2' : {
        'pergunta':'De onde é a invenção do chuveiro elétrico?',
        'respostas':{'a':'Inglaterra','b':'França','c':'Brasil','d':'Itália',},
        'resposta_correta':'c',
    },
        'pergunta 3' : {
        'pergunta':'Quais o menor e o maior país do mundo?',
        'respostas':{'a':'Vaticano e Rússia','b':'Nauru e China','c':'São Marino e Índia','d':'Mônaco e Canadá',},
        'resposta_correta':'a',
    },
        'pergunta 4' : {
        'pergunta':'Qual o nome do presidente do Brasil que ficou conhecido como Jango?',
        'respostas':{'a':'Jânio Quadros','b':'João Goulart','c':'João Figueiredo','d':'Jacinto Anjos',},
        'resposta_correta':'b',
    },
        'pergunta 5' : {
        'pergunta':'Qual o grupo em que todas as palavras foram escritas corretamente?',
        'respostas':{'a':'Asterístico, beneficiente, meteorologia, entertido','b':'Asterisco, beneficente, meteorologia, entretido','c':'Asterisco, beneficente, metereologia, entretido','d':'Asterístico, beneficiente, metereologia, entretido',},
        'resposta_correta':'b',
    },
        'pergunta 6' : {
        'pergunta':'Qual o livro mais vendido no mundo a seguir à Bíblia?',
        'respostas':{'a':'O Senhor dos Anéis','b':'Dom Quixote','c':'O Pequeno Príncipe','d':'Um Conto de Duas Cidades',},
        'resposta_correta':'b',
    },
        'pergunta 7' : {
        'pergunta':'Quantas casas decimais tem o número pi?',
        'respostas':{'a':'Duas','b':'Centenas','c':'Infinitas','d':'Milhares',},
        'resposta_correta':'c',
    },
        'pergunta 8' : {
        'pergunta':'Atualmente, quantos elementos químicos a tabela periódica possui?',
        'respostas':{'a':'108','b':'118','c':'109','d':'113',},
        'resposta_correta':'b',
    },
        'pergunta 9' : {
        'pergunta':'Quais os países que têm a maior e a menor expectativa de vida do mundo?',
        'respostas':{'a':'Japão e Serra Leoa','b':'Itália e Chade','c':'Brasil e Congo','d':'Estados Unidos e Angola',},
        'resposta_correta':'a',
    },
        'pergunta 10' : {
        'pergunta':'Qual o número mínimo de jogadores numa partida de futebol?',
        'respostas':{'a':'10','b':'8','c':'9','d':'7',},
        'resposta_correta':'d',
    },
}
print()
os.system('cls')
pontuacaoGeral = 0
print('Perguntas e Respostas, selecione uma alternativa para cada pergunta e descubra sua pontuação total\nao final das 10 perguntas. ')
for pk,pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')
    print('Alternativas:')
    for rk,rv in pv['respostas'].items():
        print(f'[{rk}]: {rv}')
    print(f'Pontuação: {pontuacaoGeral}')
    resp_usuario = input('Escolha uma alternativa: ')
    if resp_usuario == pv['resposta_correta']:
        os.system('cls')
        print('Acertou! +1 ponto')
        pontuacaoGeral +=1
    else:
        os.system('cls')
        print('Errou, siga tentando.')
    
    print()

print(f'Jogo finalizado, sua pontuação foi de {pontuacaoGeral} pontos, você acertou {pontuacaoGeral} respostas.')
print(f'Sua porcentagem de acerto foi de {(pontuacaoGeral/10)*100:.0f}%')
