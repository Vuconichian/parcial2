from grafo import Grafo  # Asegúrate de que el módulo de Grafo esté correctamente importado

mi_grafo = Grafo(dirigido=False)  # Crea un grafo no dirigido


#Punto A
print("Punto A")

mi_grafo.insert_vertice('Princesa leia')
mi_grafo.insert_vertice('R2-D2')
mi_grafo.insert_vertice('Luke skywalker')
mi_grafo.insert_vertice('BB-8')
mi_grafo.insert_vertice('Han solo')
mi_grafo.insert_vertice('Chewbacca')
mi_grafo.insert_vertice('Yoda')
mi_grafo.insert_vertice('Boba Fett')
mi_grafo.insert_vertice('Darth Vader')
mi_grafo.insert_vertice('Kylo Ren')
mi_grafo.insert_vertice('C-3PO')
mi_grafo.insert_vertice('Rey')


mi_grafo.insert_arist('Leia', 'Boba Fett', 3)
mi_grafo.insert_arist('Boba Fett', 'Rey', 1)
mi_grafo.insert_arist("luke skywalker", "princesa leia", 5)
mi_grafo.insert_arist('Boba Fett', 'C-3PO', 2)
mi_grafo.insert_arist("luke skywalker", "han solo", 4)
mi_grafo.insert_arist('Kylo Ren', 'Leia', 1)
mi_grafo.insert_arist("princesa leia", "han solo", 3)
mi_grafo.insert_arist("han solo", "chewbacca", 6)
mi_grafo.insert_arist("luke skywalker", "yoda", 2) 
mi_grafo.insert_arist('R2-D2', 'BB-8', 2)
mi_grafo.insert_arist('Luke Skywalker', 'Kylo Ren', 2)
mi_grafo.insert_arist('Luke Skywalker', 'Leia', 3)
mi_grafo.insert_arist('Leia', 'C-3PO', 4)
mi_grafo.insert_arist('Leia', 'Rey', 5)
mi_grafo.insert_arist('C-3PO', 'Rey', 3)
mi_grafo.insert_arist('Chewbacca', 'Han Solo', 4)
mi_grafo.insert_arist('Yoda', 'Chewbacca', 1)
mi_grafo.insert_arist('Luke Skywalker', 'Darth Vader', 5)


#Punto B
print("Punto B")
arbol_de_expansion_minina = mi_grafo.kruskal()

# Verificar si Yoda está presente en el bosque MST
yoda_presente = False
for arista in arbol_de_expansion_minina:
    if "yoda" in arista:
        yoda_presente = True
        break

if yoda_presente:
    print("Yoda está presente en el arbol de expansion minima")
else:
    print("Yoda no está presente en el arbol de expansion minina")


#Punto C
print("Punto C")
max_episodios, personajes_max_episodios = mi_grafo.encontrar_max_episodios_compartidos()
print(f"El número máximo de episodios compartidos es {max_episodios}.")
print(f"Los personajes que comparten este número máximo de episodios son: {', '.join(personajes_max_episodios)}")