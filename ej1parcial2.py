from arbol_binario import BinaryTree

lista_pokemons = [
    {'nombre': 'bulbasaur', 'tipo': ['planta', 'veneno'], 'numero': 1},
    {'nombre': 'charizard', 'tipo': ['fuego', 'volador'], 'numero': 6},
    {'nombre': 'pikachu', 'tipo': ['eléctrico'], 'numero': 25},
    {'nombre': 'mewtwo', 'tipo': ['psíquico'], 'numero': 150},
    {'nombre': 'gyarados', 'tipo': ['agua', 'volador'], 'numero': 130},
    {'nombre': 'eevee', 'tipo': ['normal'], 'numero': 133},
    {'nombre': 'gengar', 'tipo': ['fantasma', 'veneno'], 'numero': 94},
    {'nombre': 'machop', 'tipo': ['lucha'], 'numero': 66},
    {'nombre': 'lapras', 'tipo': ['agua', 'hielo'], 'numero': 131},
    {'nombre': 'snorlax', 'tipo': ['normal'], 'numero': 143},
    {'nombre': 'mudkip', 'tipo': ['agua'], 'numero': 258},
    {'nombre': 'rayquaza', 'tipo': ['dragón', 'volador'], 'numero': 384},
    {'nombre': 'lucario', 'tipo': ['lucha', 'acero'], 'numero': 448},
    {'nombre': 'greninja', 'tipo': ['agua', 'siniestro'], 'numero': 658},
    {'nombre': 'sylveon', 'tipo': ['hada'], 'numero': 700},
    {'nombre': 'lycanroc', 'tipo': ['roca'], 'numero': 745},
    {'nombre': 'tyrantrum', 'tipo': ['roca', 'dragón'], 'numero': 697},
    {'nombre': 'jolteon', 'tipo': ['eléctrico'], 'numero': 135}
]



print()
# Punto A
print('Punto A')
name_tree = BinaryTree()
type_tree = BinaryTree()
number_tree = BinaryTree()
print("Name tree, Specie tree y Type tree han sido creadas")
print()

for pokemon in lista_pokemons:
    name = pokemon['nombre']
    number = pokemon['numero']
    types = pokemon['tipo']

    name_tree.insert_node(name)

    number_tree.insert_node(number)

    for type in types:
        type_tree.insert_node(type, {"nombre": name, "numero": number})


print()
# Punto A
print('Punto A')
name_tree = BinaryTree()
specie_tree = BinaryTree()
ranking_tree = BinaryTree()
print("Name tree, Specie tree y Ranking tree han sido creadas")
print()

print()
for pokemon in lista_pokemons:
    nombre = pokemon.get("nombre")
    name_tree.insert_node(nombre, pokemon)

print()

for pokemon in lista_pokemons:
    numero = pokemon.get("numero") 
    number_tree.insert_node(numero, pokemon) 

print()

#Punto B
print('Punto B')
print()
print("Información de un pokemon en particular:")
name_tree.inorden_start_with_("bul")
print()


print('Punto C')
print("Pokemons ordenados por tipo':")
name_tree.inorden_start_with_tipo("agua")
print()


#Punto D
print('Punto D')
print()
print('Barrido inorden de pokemons ordenados por nombre:')
name_tree.inorden()
print()
print('Barrido inorden de pokemons ordenados por numero:')
number_tree.inorden()
print()
print('Barrido por nivel de pokemons ordenados por nombre:')
name_tree.by_level()


#Punto E
print('Punto E')
print()
print("Información de Jolteon:")
name_tree.inorden_start_with_("jolteon")
print()
print("Información de Lycanroc:")
name_tree.inorden_start_with_("lycanroc")
print()
print("Información de Tyrantrum:")
name_tree.inorden_start_with_("tyrantrum")
print()

#Punto F
print('Punto F')
electricos_count = type_tree.contar("eléctrico")
acero_count = type_tree.contar("acero")

print(f"Cantidad de Pokémon eléctricos: {electricos_count}")
print(f"Cantidad de Pokémon de acero: {acero_count}")