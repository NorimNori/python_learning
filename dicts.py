# DICCIONARIO: colección (array) que permite almacenar múltiples elementos en una sola variable.
# Características: Colección de pares clave-valor(key-value) desordenada y mutable.
# Permiten diferentes tipos de datos pero no duplicados.

diccionario = {
    "nombre": "Cillian Murpfy",
    "youtube": "www.youtube.com/@cillian",
    "tecnologias": ["Python", "Javascript"],
    "edad": 34,
    "direccion": {"calle": "Oxford", "numero": 123, "ciudad": "Londres"},
}

tipo = type(diccionario) # Nos indica el tipo de dato <class 'dict'>.
longintud = len(diccionario) # Nos indica la cantidad de claves-valor que tiene el diccionario.
contructorDiccionario = dict(nombre = "Cillian Murphy", youtube = "www.youtube.com/@cillian") # Se puede crear con constructor.

# ¿Cómo accedo a cada propiedad?

nombre = diccionario["nombre"]
youtube = diccionario.get("youtube") # Otra manera de acceder al valor de una key.
keys = diccionario.keys() # el tipo de dato que devuelve se llama <class 'dict_keys'> (un diccionario de keys).
values = diccionario.values() # el tipo de dato que devuelve se llama <class 'dict_values'> (un diccionario de valores).

items = diccionario.items() # nos devuelve tuplas de clave-valor en una lista // <class 'dict_items' (diccionario de items o tuplas value-key)>.

if "tecnologias" in diccionario: # Con esto podemos comprobar si una key existe pero no un valor.
    print("Sí, existe esta key")

# CAMBIO de valores en un diccionario.

diccionario["tecnologias"] = ['Python', 'JavaScript', 'Java', 'Node']
diccionario.update({"direccion": {"calle": "Liverpool Street", "numero": 123, "ciudad": "Londres"},})

# AGREGAR ITEMS:

diccionario["profesion"] = "Programador"
diccionario.update({ 'Comida Favorita': ' Milanesa'}) #Funciona exactamente igual.

# ELIMINAR ITEMS:

diccionario.pop("Comida Favorita") # Eliminar un elemento puntual.
diccionario.popitem() # Eliminaría última característica agregada.
del diccionario["edad"] # Funciona como la opcion POP.
diccionario.clear() # esto deja vacío el diccionario.

# BUCLES (LOOPS ) para diccionarios:

curso_python = {
    "nombre": "Python desde Cero",
    "duracion": 6,
    "dificultad": "media",
}

for key in curso_python: # el bucle for común hará un recorrido de las keys (unicamente las keys).
    print(f"{key.capitalize()}: {curso_python[key]}")

for values in curso_python.values(): # este bucle recorrerá solo los valores.
    print(values)

for key, value in curso_python.items(): # desempaqueto la tupla de cada uno de los elementos de la lista que devuelve items.
    print(key, value)

# COPIAS de diccionarios:

copia = curso_python.copy() # copia exacta pero apuntando a otra dirección de memoria.
copia2 = dict(curso_python) # copia usando constructor.

# DICCIONARIOS ANIDADOS:

hijo1 = {
    "nombre" : "Hugo",
    "edad" : 5
}
hijo2 = {
    "nombre" : "Paco",
    "edad" : 9
}
hijo3 = {
    "nombre" : "Luis",
    "edad" : 13
}

# Primero se declararon los diccionarios por fuera y luego se asignaron a cada llave del dict. familia (funciona igual que declarar dentro del diccionario padre).
familia = {
    "hijo1": hijo1,
    "hijo2": hijo2,
    "hijo3": hijo3,
}

nombreHijo1 = familia["hijo1"]["nombre"]

# Primero se itera el obj familia.
for x,obj in familia.items():
    print(x)
    # Luego se itera el obj anidado para obtener los elementos.
    for y in obj:
        print(f"{y.capitalize()}: {obj[y]}")