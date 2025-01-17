# Superclase = clase padre.

class GreekGod:
    def __init__(self, name, domain):
        self.name = name
        self.domain = domain

    def introduce(self):
        print(f"I am {self.name}, the god of {self.domain}.")

# Subclase = clase hija.

class Athena(GreekGod):
    def __init__(self, name, domain, symbol):
        ## super() se encarga de mandar la informacion de los atributos a la superclase, en este caso name y domain.
        super().__init__(name, domain)
        ## se inicializa el atributo propio de la subclase.
        self.symbol = symbol
    
    ## metodo propio de la subclase Athena.
    def show_wisdom(self):
        print(f"{self.name} uses her symbol of {self.symbol} to impart wisdom and strategy.")

class Hades(GreekGod):
    def __init__(self, name, domain, guardian):
        super().__init__(name, domain)
        self.guardian = guardian

    ## metodo propio de la subclase Hades.
    def summon_guardian(self):
        print(f"{self.name}, lord of the {self.domain}, summons his guardian, {self.guardian}, to protect his realm.")

## se craen las instancias de cada clase
athena = Athena("Athena", "wisdom and strategy", "the owl")
hades = Hades("Hades", "the underworld", "Cerberus")

## las subclases no solo heredan los atributos, tambien los metodos de la superclase.
athena.introduce()
hades.introduce()

## las subclases pueden tener sus propios metodos.
athena.show_wisdom()
hades.summon_guardian()