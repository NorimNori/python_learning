# Superclase:
class Instrument():
    def __init__(self, name):
        self.name = name

    def play(self):
        print("Making a generic sound")

# subclase
class Drums(Instrument):
    def __init__(self):
        super().__init__("The drums")

    # sobreescribir el metodo con un comporamiento propio de esta clase (OVERRIDE).
    def play(self):
        print(f"\033[92m{self.name} is keeping a solid 4/4 rhythm with the snare and bass drum")

# subclase
class Harmonica(Instrument):
    def __init__(self):
        super().__init__("The harmonica")
    
    # override
    def play(self):
        print(f"\033[93m{self.name} is playing a soulful blues melody")

#subclase
class Mandolin(Instrument):
    def __init__(self):
        super().__init__("The mandolin")

    # override
    def play(self):
        print(f"\033[94m{self.name} is strumming an uplifting folk tune")

# instancias.
drums = Drums()
harmonica = Harmonica()
mandolin = Mandolin()

"""
Polimorfismo: Es la capacidad de un método o función para comportarse de manera diferente según el tipo de objeto o clase que lo invoque. 
Esto permite que el mismo método pueda ser utilizado por objetos de diferentes clases, 
pero con implementaciones específicas para cada una de ellas.
"""

drums.play()
harmonica.play()
mandolin.play()
