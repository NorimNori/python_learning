from abc import ABC, abstractmethod

# Clase abstracta: la plantilla o modelo de las clases que la hereden.
"""
Una clase BASE es simplemente una clase común que otras clases pueden heredar 
y la ABSTRACTA no se puede instanciar estando sólo hecha para darle forma a las hijas.
"""

class Animal(ABC):
    # Atributo estático (atributo de clase): va a estar disponible independientemente de las instancias.
    cant_animales = 0

    def __init__(self, name):
        self.name = name
        Animal.cant_animales += 1

    # Un método abstracto de esta forma obliga a las clases derivadas a implementar este comportamiento.
    @abstractmethod
    def make_sound(self):
        pass

    # Método de clase: es un método que se puede ejecutar desde la clase misma.
    # cls: se refiere a la clase [Al ser un atributo estático le pertenece a la clase y no a la instancia].
    @classmethod
    def get_animal_count(cls):
        print(f"The current number of animals is: {cls.cant_animales}")

# Subclase: Rock hyrax
class Rock_hyrax(Animal):
    def make_sound(self):
        print("He screams 'Awawaaaaa!!' when he sees you.")
    
    # Método propio de la clase Rock_hyrax
    def run(self):
        print(f"{self.name} is running across the dunes!")

# Subclase: Willow ptarmigan
class Willow_ptarmigan(Animal):
    def make_sound(self):
        print("He says 'awebo' all day.")
    
    # Método propio de la clase Willow_ptarmigan
    def fly(self):
        print(f"{self.name} is flying through the snow-covered landscape!")

# Crear instancias
rock_hyrax = Rock_hyrax("Cheto")
willow_ptarmigan = Willow_ptarmigan("Rufle")

# Llamar a los métodos
rock_hyrax.run()
rock_hyrax.make_sound()
willow_ptarmigan.fly()
willow_ptarmigan.make_sound()

# Obtener el conteo de animales
print('-' * 55)
Animal.get_animal_count()
