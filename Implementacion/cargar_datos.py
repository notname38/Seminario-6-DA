import numpy as np
import os

################################################
################################################

# Carga de datos:
def leer_instancia(filepath):

    fp=open(filepath)

    # La primera línea -> número de vértices.
    line=fp.readline()
    values=line.split()
    n_vertices=int(values[0])
    
    # En la segunda línea -> número de aristas.
    line=fp.readline()
    values=line.split()
    n_aristas =int(values[0])

    # Por cada linea siguiente 3 numeros:
        # Primer numero: Arista
        # Segundo numero: Arista
        # Tercer numero: Peso entre ellas   
    grafo=np.zeros((n_aristas,3))
    for i in range(n_aristas):
        line=fp.readline()
        values=line.split()
        for j in range(3):
            grafo[i][j] = values[j]
    fp.close()

    return (n_vertices, n_aristas, grafo)

################################################
################################################

# # Test:
# print("Test cargar_datos: ")
# print(" ")
# print(" ")

# path = os.path.abspath(os.path.join(os.getcwd(), os.pardir)) + "/Implementacion/Datos/"

# test_elements = [
#     "mst8n16a_tiny.txt",
#     "A5_ZikloaDuGZ.txt",
#     "HZM_n8_a11_134.txt"
# ]

# for name in test_elements:
#     newPath = path + name
#     n_vertices, n_aristas, datos = leer_instancia(newPath)
#     print("Nombre: " + name)
#     print("Path: " + newPath)
#     print("Numero de vertices: ", n_vertices)
#     print("Numero de aristas: ", n_aristas)
#     print(" ")
#     print("Estructura de memoria: ")
#     G = Grafo(n_vertices)
#     G.cargar_grafo(datos)
#     print(G.grafo)
#     print(" ")
#     print(" ")

