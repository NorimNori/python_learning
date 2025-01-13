# str (string): Texto o cadena de caracteres
comillasSimples = 'Este es un texto'
comillasDobles = "Este es un texto"
comillasTriples = """Este es un texto"""
comillasTriplesSimples = '''Este es un texto'''

# int (Integer): Número entero
numero_entero = 1
print("Entero o Integer: ", numero_entero)

# float: Número decimal.
# Solo tiene 16 espacios de memoria. El ultimo es redondeado.
numero_decimal = 3.718281828459045
print("Decimal o Float: ", numero_decimal)

# complex: numero complejo (parte entera y otra parte imaginaria).
numero_complejo = 5 + 2j
print("Complejo o Complex: ", numero_complejo)

# list[]: Colección ordenada y mutable de elementos (cada elemento tendrá un índice).
lista = [0,1,2,3,4,5,5,5]
print("Lista o Array: ", lista)

# tuple(): Colección ordenada e inmutable de elementos (cada elemento tendrá un índice).
tupla = ("a", "b", "c")
print("Tupla o Tuple: ", tupla)

# range: Es una secuencia de números generada dentro de un rango. Sin incluir en 10. 
rango = range(1,10)
print("Rango o Range", rango)

# dict (dictionary){}: Colección de pares clave-valor(key-value) desordenada y mutable.
diccionario = {"nombre": "Sergie Code"}
print("Diccionario o Dict: ", diccionario)

# set{}: Coleccion desordenada de elementos únicos y MUTABLES.
conjunto = {1,1,2,2,3}
print("Conjunto o Set", conjunto)
# // {1,2,3} 

# frozenSet([]): Colección desordenada de elemento únicos e INMUTABLES.
conjunto_inmutable = frozenset([1,2,3,3,3])
print("Conjunto inmutable o frozenSet", conjunto_inmutable)
# // {1,2,3} 

# bool (booleanos): valor verdadero o falso (true/false).
booleanoVerdadero = True
booleanoFalso = False
print("Booleanos o Boolean: ", booleanoVerdadero, booleanoFalso)