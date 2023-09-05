from vehiculo import Vehiculo

class Moto(Vehiculo):
    #definimos el constructor con sus respectivos atributos de la clase Vehiculo, ademas se agregaron
    #los atributos propios de la clase como son: marca, modelo y nivelGasolina
    def __init__(self, velocidadMaxima, capacidadTanque, marca, modelo, nivelGasolina):
        super().__init__(velocidadMaxima, capacidadTanque)
        self.marca = marca
        self.modelo = modelo
        self.nivelGasolina = nivelGasolina
    
    #definimos el metodo acelerar el cual aumenta la velocidad del vehiculo en 20 km/h
    def acelerar(self):
        self.velocidadActual += 20
    
    #definimos el metodo frenar el cual disminuye la velocidad del vehiculo en 5 km/h
    def frenar(self):
        self.velocidadActual -= 5
        