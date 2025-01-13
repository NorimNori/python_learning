##### OPERADORES: símbolos que nos permitirán hacer operaciones sobre variables y valores.

## Operadores aritméticos (+,-,*,/,%,**,//).

a = 11
b = 5

suma = a + b
resta = a - b
multiplicacion = a * b
division = a / b # devuelve flotante (con decimales).
floorDivision = a // b  # devuelve un entero.
resto = a % b # Resto de la división.
exponenciacion = a ** b 

## Operadores de asignación.

x = 10 # El = es el operador de asignación más básico. 
x += 3 # El += le suma el valor al valor anterior.
x -= 2 # El -= le resta el valor al valor anterior.
x *= 2 # El *= le multiplica el valor al valor anterior.
x /= 2 # El /= le dividie el valor al valor anterior.
x //= 2 
x %= 1
x **= 2

## Operadores de comparación (devuleven un booleano).

num1 = 6
num2 = 5
igualdad = num1 == num2 # Devuelve True si son iguales.
distintos = num1 != num2 # Devuelve True si son distintos.
mayor = num1 > num2 # Devuelve True si es Mayor.
menor = num1 < num2 # Devuelve True si es Menor.
mayorOIgual = num1 >= num2 # Devuelve True si es Mayor o Igual.
menorOIgual = num1 <= num2 # Devuelve True si es Menor o Igual.

## Operadores lógicos (and, or, not).
edad = 17
tramite = edad >= 18 and edad <= 65 ## Devuelve True si cumplimos las las 2 condiciones dadas.
semaforo = "Rojo"
cruzar = semaforo == "Verde" or semaforo == "Amarillo" # Devuelve True si cumplimos al menos una de las dos condiciones.
verdad = True
negacion = not verdad # Niega la estructura siguiente. Es basicamente negar.

## Operadores de identidad (is, is not).
nombre = "Luis"
profesor = "Luis"
alumno = "Paco"
sonElMismo = nombre is profesor #  Compara igualdad, nos devuelve True si son iguales.
sonDistintos = profesor is not alumno #  Compara diferencia, nos devuelve True si son distintos.

## Operadores de pertencia (in, not in).
palabra = "Hola Mundo"
palabra2 = "Marte"
texto = "Hola Mundo"
pertenece = palabra in texto # Compara pertenecia, nos devuelve True si pertenece.
noPertenece = palabra2 not in texto # Compara no pertenencia, nos devuelve True si no está presente.

