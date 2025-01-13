####### NUMBERS

# int (Integer): Número entero.
numero_entero = 10

# float: Número decimal.
numero_decimal = 5.75

# complex: numero complejo (parte entera y otra parte imaginaria).
numero_complejo = 5 + 2j
# Para saber el tipo de dato se utiliza type().
print(numero_entero) 
print(type(numero_entero)) # int

print(numero_decimal) #3.14
print(type(numero_decimal)) #float

print(numero_complejo)  # (5+2j)
print(type(numero_complejo))  # complex

###### CASTEO (Cambiar el tipo de dato).

decimal_desde_entero = float(numero_entero)
# En este caso únicamente ser corta la parte decimal y no se redondea.
entero_desde_decimal = int(numero_decimal)
complejo_desde_entero = complex(numero_entero)
complejo_desde_decimal = complex(numero_decimal)

print(decimal_desde_entero)
print(entero_desde_decimal)
# // 5
print(complejo_desde_entero)
print(complejo_desde_decimal)
# No se puede cambiar un entero o decimal desde un complejo ya que no se resulven de esta manera los números imaginarios.

####### RANDOM
# Normalmente los imports deben colocarse al inicio del documento.
import random

aleatorio = random.randrange(1,10) # El número de stop no es incluyente.
aleatorio_par = random.randrange(2,11,2) # Número par del 2 al 10 (incluído).
aleatorio_impar = random.randrange(1,10,2) #Número impar del 1 al 9 (incluído).

print(aleatorio)
print(aleatorio_par)
print(aleatorio_impar)