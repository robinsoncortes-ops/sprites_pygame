# Deficion de la clase de vehiculo
class vehiculo:

    # constructor del vehiculo
    def __init__(self,matricula, color, numeroPuertas):
        self.MATRICULA = matricula
        self.COLOR = color
        self.NUMERO = numeroPuertas
        self.AVANZA = False
        print("construccion de un vehiculo : " + self.MATRICULA)

    # metodo avanzar
    def Avanzar(self):
        self.AVANZA = True
        print(self.MATRICULA + " avanza.")

    # metodo detenerse
    def Detenerse(self):
        self.AVANZA = False
        print(self.MATRICULA + " se detiene.")


# construccion de una primera instancia
vehiculo1 = vehiculo("RB123", "rojo", 4 )

#construccion de una segunda instancia 
vehiculo2 = vehiculo("KL345", "verde", 4 )

# El primer vehiculo avanza
vehiculo1.Avanzar()

# El primer vehiculo se detiene
vehiculo1.Detenerse()

# entre la linea (1,2) es para iniciar con el programa
# entre la linea (4,10) es para colocarle la matricula, color , numero de puertas para la construcion del vehiculo
# entre la linea (12,20) es para que el vehiculo avanze o se detenga
# entre la linea (23,33) es para que el programa imprima las condiciones que nosotros mismos le colocamos
