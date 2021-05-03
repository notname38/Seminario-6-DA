import sys 

################################################
################################################

def kruskal(G):
    i = 0
    e = 0
    pesoMinimo = 0

    G.grafo = sorted(G.grafo, key=lambda item: item[2])

    raiz = []
    profundidad = []
    resultado = []  
 
    for elemento in range(G.nVertices):
        raiz.append(elemento)
        profundidad.append(0)
 
    while e < G.nVertices - 1:
        v1, v2, peso = G.grafo[i]
        i = i + 1
        c1 = G.buscar(raiz, v1)
        c2 = G.buscar(raiz, v2)
        if c1 != c2:
            e = e + 1
            resultado.append([v1, v2, peso])
            pesoMinimo = pesoMinimo + peso
            G.union(raiz, profundidad, c1, c2)
 
    return resultado, pesoMinimo

################################################
################################################

def prim(G):

    pesos = [sys.maxsize] * G.nVertices
    pesos[0] = 0 
    raiz = [None] * G.nVertices
    raiz[0] = -1 
    arbol = [False] * G.nVertices
    resultado = []
    pesoMinimo = 0
  
    for aux in range(G.nVertices):
        # Selecionar minimo.
        i = G.funcionMin(pesos, arbol)

        arbol[i] = True
        for j in range(G.nVertices):
            if G.grafo[i][j] > 0 and arbol[j] == False and pesos[j] > G.grafo[i][j]:
                pesos[j] = G.grafo[i][j]
                raiz[j] = i
  
    for i in range(1, G.nVertices):
        pesoMinimo = pesoMinimo + G.grafo[i][raiz[i]]
        resultado.append([raiz[i], i, G.grafo[i][raiz[i]]])
    
    return resultado, pesoMinimo
  