"""
Aula 19 - For e Else em python
"""

var = ['Lucas', 'João', 'Izabella']

Linit = False

for n in var:
    if n.lower().startswith('l'):   #Serve tanto para maiúsculo quanto para minúsculo
        Linit = True
if Linit:
    print('Existe')
else:
    print('não existe')
