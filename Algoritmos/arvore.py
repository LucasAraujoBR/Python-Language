class NodoArvore:
    def __init__(self, chave=None, esquerda=None, direita=None):
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita

    def __repr__(self):
        return '%s <- %s -> %s' % (self.esquerda and self.esquerda.chave,
                                    self.chave,
                                    self.direita and self.direita.chave)

def insere(raiz, nodo):
    # """Insere um nodo em uma árvore binária de pesquisa."""
    # Nodo deve ser inserido na raiz.
    if raiz is None:
        raiz = nodo

    # Nodo deve ser inserido na subárvore direita.
    elif raiz.chave < nodo.chave:
        if raiz.direita is None:
            raiz.direita = nodo
        else:
            insere(raiz.direita, nodo)

    # Nodo deve ser inserido na subárvore esquerda.
    else:
        if raiz.esquerda is None:
            raiz.esquerda = nodo
        else:
            insere(raiz.esquerda, nodo)

def busca(raiz, chave):
    """Procura por uma chave em uma árvore binária de pesquisa."""
    # Trata o caso em que a chave procurada não está presente.
    if raiz is None:
        return None

    # A chave procurada está na raiz da árvore.
    if raiz.chave == chave:
        return raiz

    # A chave procurada é maior que a da raiz.
    if raiz.chave < chave:
        return busca(raiz.direita, chave)

    # A chave procurada é menor que a da raiz.
    return busca(raiz.esquerda, chave)

# 50, 10, 40, 90, 78, 54, 34, 2
# 2 , 10, 34 , 40 , 50 , 54 , 78, 90
raiz = NodoArvore(40)

raiz.esquerda = NodoArvore(10)
raiz.direita  = NodoArvore(54)

raiz.direita.esquerda  = NodoArvore(50)
raiz.direita.direita   = NodoArvore(78)
raiz.direita.direita.direita   = NodoArvore(90)

raiz.esquerda.esquerda = NodoArvore(2)
raiz.esquerda.direita  = NodoArvore(34)


print('            ',raiz.chave)
print(raiz.esquerda,raiz.direita)
print(raiz.esquerda.esquerda,raiz.direita.direita)


# Cria uma árvore binária de pesquisa.
raiz = NodoArvore(76)
for chave in [2,10,1,79,78,90]:
    nodo = NodoArvore(chave)
    insere(raiz, nodo)

print('          ',raiz.chave)
print(raiz.esquerda,raiz.direita)


# Procura por valores na árvore.
for chave in [-50, 10, 30, 70, 100]:
    resultado = busca(raiz, chave)
    if resultado:
        print("Busca pela chave {}: Sucesso!".format(chave))
    else:
        print("Busca pela chave {}: Falha!".format(chave))