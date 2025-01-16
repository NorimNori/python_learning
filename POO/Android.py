# CLASE (CLASS): plantilla que define caracteristicas y comportamientos de un objeto.

class Android:
    ## Constructor: metodo especial que se ejecuta al crear una instancia y se encarga de inicializar los atributos.
    ## Self apunta a la intancia en si.
    def __init__(self, name, type):
        ## Atributos o caracteristicas
        self.name = name
        self.type = type

# Instancia: objeto especifico creado a partir de la clase.
android_A = Android("No. 17", "Male")

print(android_A.name)
## > No. 17
print(android_A.type)
## > Male