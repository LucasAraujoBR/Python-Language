import os



d1 = {'Nome da Chave':'Valor da chave'}
d1['Nova_chave'] = 'valor da nova chave'
print(d1['Nome da Chave'])
print(d1)



#Outra forma de criar dicionarios
d2 = dict(chave1 = 'valorando',chave2=5)
print(d2['chave1'],d2['chave2'])
print(d2)

#Del - deleta valores updade - modifica valores

#maneira de encontrar valores no dicionario

d3={
    'str': 'valor',
    123: 'outro valor',
    (1,2,3,4): 'tupla',

}

print('str' in d3)
print('str' in d3.keys())
print('valor' in d3.values())


#Saber quantos pares tem 
print(len(d3))


#leitura de valores
for k in d3.values():
    print(k)

#leitura completa
for k in d3.items():
    print(k)

for k, v in d3.items():
    print(k, v)

os.system('cls') #Função limpa tela da biblioteca os 'clear'(Na CMD) 'cls'(No PowerShell)

clientes ={
    'Cliente1':{
        'Nome' : 'Lucas Edson',
        'CPF'  : '123.123.456-85',
    },
    'Cliente2':{
        'Nome'  :  'Maria Izabella',
        'CPF'   :  '951.753.852.00',
    },
}

for clientes_k,clientes_v in clientes.items():
    print(f'Exibindo{clientes_k}')
    for dados_Cliente_k,dados_Cliente_v in clientes_v.items():
        print(f'\t{dados_Cliente_k} = {dados_Cliente_v}')


os.system('cls')

#copia do dicionario
print(clientes)
v = clientes.copy() #copia básica 
print(v)

import copy

z = copy.deepcopy(clientes) #copia completa deixando z independente de clientes
