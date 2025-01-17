class Safe: 
    def __init__(self, pin, amount):
        self.__pin = pin
        self.__amount = amount

    # Getters: metodos para obtener información de un atributo privado.
    #def obtener_clave(self):
    #return self.__clave
    
    ## verificar que el pin sea correcto.
    def check_pin(self, pin):
        return self.__pin == pin # Devolverá TRUE si la clave que nos pasan coincide con la original.
    
    ## obtener la cantidad de la cuenta.    
    def get_amount(self, pin):
        if self.check_pin(pin):
            return self.__amount
        else:
            print("Incorrect PIN!")

    # Setters: metodos para establecer nuevos valores a los atributos privados.

    ## ingresar un pin.
    def set_pin(self, new_pin, pin):
        if self.check_pin(pin):
            # se verifica que el PIN tenga 4 digitos exactamente y que sean numeros.
            if len(new_pin) != 4 or not new_pin.isdigit():
                print("The PIN must be 4 digits")
            else:
                print("The PIN was changed successfully")
                self.__pin = new_pin
        else:
            print("Incorrect PIN!")
    ## ingresar una catidad.
    def set_amount(self, new_amount, pin):
        if self.check_pin(pin):
            ## try se encarga de manejar errores que podrian ocurrir en el programa.
            try:
                # se convierte new_amount a un entero para evitar errores de comparacion str con int.
                new_amount = int(new_amount)
            # Si no es un numero valido, lanza una excepcion.
            ## except se ejecuta solo si se ha generado un error, en este caso de tipo ValueError.
            except ValueError:
                print("The new amount must be a number")
                return
            
            # se verifica que la cantidad ingresada no sea negativo o igual a 0.
            if new_amount <= 0:
                print("You cannot enter a negative or zero amount")
            else:
                print("The AMOUNT was changed successfully")
                self.__amount = new_amount
        else:
            print("Incorrect PIN!")


safe = Safe("1234", 1000)

safe.set_pin("4567", "1234")
safe.set_amount("7000", "4567")

print(safe.get_amount("4567"))