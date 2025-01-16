# CLASE (CLASS): plantilla que define caracteristicas y comportamientos de un objeto.

# Se debe declarar con mayuscula.
class Android:
    ## Constructor: metodo especial que se ejecuta al crear una instancia y se encarga de inicializar los atributos.
    ## Self apunta a la intancia en si.
    def __init__(self, name, type):
        ## Atributos o caracteristicas
        self.name = name
        self.type = type

    # Metodo: es una funcion que define el comportamientoo accion de un objeto
    def greet(self):
        print("Hola. No pierdas mi tiempo, ¿de acuerdo?")

    def presentation(self):
        if self.type == "Male":
            print(f"¿Te interesa saber quién soy? Soy el {self.name}. Aunque no creo que importe mucho para ti.")
        else:
            print(f"{self.name} No te preocupes por recordarlo, no durará mucho.")

# Instancia: objeto especifico creado a partir de la clase.
android_A = Android("No. 17", "Male")
android_B = Android("No.18.", "Female")

## Utilizamos los metodos de la clase en cada instacia para que se ejecuten,
android_A.greet()
android_B.greet()
android_A.presentation()
android_B.presentation()

#print(android_A.name)
## > No. 17
#print(android_A.type)
## > Male
