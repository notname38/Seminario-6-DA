from collections import defaultdict
import sys 

################################################
################################################

# Clase Grafo_particion para kruskal
class Grafo_particion:

    def __init__(self, vertices):
        self.nVertices = vertices  
        self.grafo = []  

    def anadir_arista(self, vert1, vert2, peso):
        self.grafo.append([vert1, vert2, peso])

    def cargar_grafo(self, estructura_datos):
        for arista in estructura_datos:
            self.anadir_arista(arista[0], arista[1], arista[2])

    def buscar(self, raiz, etiqueta):
        etiqueta = int(etiqueta)
        if raiz[etiqueta] != etiqueta:
            return self.buscar(raiz, raiz[etiqueta])
        return etiqueta

    def union(self, raiz, profundidad, e1, e2):

        raiz1 = self.buscar(raiz, e1)
        raiz2 = self.buscar(raiz, e2)
 
        if profundidad[raiz1] < profundidad[raiz2]:
            raiz[raiz1] = raiz2
        elif profundidad[raiz1] > profundidad[raiz2]:
            raiz[raiz2] = raiz1

        else:
            # incrementa la profundidad del primer subárbol
            raiz[raiz2] = raiz1
            profundidad[raiz1] += 1
        
################################################
################################################

# Clase Grafo para prim
class Grafo_Prim:

    def __init__(self, vertices):
        self.nVertices = vertices  
        self.grafo = []
        for fila in range(vertices):
            lis = []
            for columna in range(vertices):
                lis.append(0)
            self.grafo.append(lis)

    def anadir_arista(self, vert1, vert2, peso):
        self.grafo[int(vert1)][int(vert2)] = peso
        self.grafo[int(vert2)][int(vert1)] = peso


    def cargar_grafo(self, estructura_datos):
        for arista in estructura_datos:
            self.anadir_arista(arista[0], arista[1], arista[2])

    def funcionMin(self, pesos, arbol):
        peso_min = sys.maxsize
        for vertice in range(self.nVertices):
            if pesos[vertice] < peso_min and arbol[vertice] == False:
                peso_min = pesos[vertice]
                indice_minimo = vertice
        return indice_minimo
      

################################################
################################################
    


