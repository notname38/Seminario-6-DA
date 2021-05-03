from algoritmos import kruskal
from algoritmos import prim
from estructura_grafo_particion import Grafo_particion
from estructura_grafo_particion import Grafo_Prim
from cargar_datos import leer_instancia
import os


print("Seminario 6 DA.")
print("Ejericio 1 (Prim y Kruskal)")
print(" ")


decision = input("Por favor, presiona enter para continuar:\n")
test_elements = [
    "A5_ZikloaDuGZ",
    "mst8n16a_tiny",
    "HZM_n8_a11_134"
]
path = os.path.abspath(os.path.join(os.getcwd(), os.pardir)) + "/Implementacion/Datos/"
path_save = os.path.abspath(os.path.join(os.getcwd(), os.pardir)) + "/Implementacion/Resultados/"

for test in test_elements:
    print(" ")
    print("Procesando: " + test)
    newPath = path + test + ".txt"
    n_vertices, n_aristas, datos = leer_instancia(newPath)

    G_Kruskal = Grafo_particion(n_vertices)
    G_Prim = Grafo_Prim(n_vertices)

    G_Kruskal.cargar_grafo(datos)
    G_Prim.cargar_grafo(datos)

    print("Aplicando kruskal...")
    resultado, pesoMinimo = kruskal(G_Kruskal)
    f = open(path_save+test + "_kruskal.txt", "w")
    f.write(str(pesoMinimo))
    f.write("\n")
    f.write(str(len(resultado)))
    f.write("\n")
    for arista in resultado:
        f.write(str(arista))
        f.write("\n")
    f.close()

    print("Aplicando prim...")
    resultado, pesoMinimo = prim(G_Prim)
    f = open(path_save+test + "_prim.txt", "w")
    f.write(str(pesoMinimo))
    f.write("\n")
    f.write(str(len(resultado)))
    f.write("\n")
    for arista in resultado:
        f.write(str(arista))
        f.write("\n")
    f.close()

print(" ")
print("Terminado!")









