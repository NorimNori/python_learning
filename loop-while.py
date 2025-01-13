## BUCLES O LOOPS: estructura que se repite mientras la condición sea verdadera.
## BUCLE WHILE: 

x = 1

while x <= 10:
    # Si el print se escribe despues de la sumatoria comenzara en 2 y terminara en 11.
    print(f"Hola a todos estoy dentro de un bucle y x vale {x}")
    x += 1

    # Si queremos salir del bucle podemos agregar una condicion y agregar la palabra reservada BREAKE.
    if x == 5:
        break # Esto hace que salga del bucle y de aqui en adelante no se cumple nada.

    if x == 15:
        continue # Corta el bucle en el momento en que esta y vuleve a empezar. Puede dar un bucle infinito si no se usa correctamente.

else:
    print(f"Ya no se cumplió la condición del bucle porque x es {x}")

## EJEMPLO PRACTICO.

while True:
    print("No te olvides de comprar mis chocolates")
    respuesta = input("¿Ya has comprado los chocolates? (s/n)").strip().lower()
    if respuesta == 's':
        break