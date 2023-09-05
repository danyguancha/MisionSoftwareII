from vehiculo import Vehiculo
class Coche(Vehiculo):
    #definimos el constructor con sus respectivos atributos de la clase Vehiculo, ademas se agregaron
    #los atributos propios de la clase como son: marca, modelo y nivelGasolina
    def __init__(self, velocidadMaxima, capacidadTanque, marca, modelo, nivelGasolina):
        super().__init__(velocidadMaxima, capacidadTanque)
        self.marca = marca
        self.modelo = modelo
        self.nivelGasolina = nivelGasolina
        self.turbo = False
    
    #definimos el metodo de acelerar el cual activa el turbo del vehiculo
    def activarTurbo(self):
        self.turbo = True
    
    #definimos el metodo desactivarTurbo el cual desactiva el turbo del vehiculo
    def desactivarTurbo(self):
        self.turbo = False  
    
    #definimos el metodo acelerar el cual aumenta la velocidad del vehiculo en 30 km/h,
    #si el turbo esta activado, de lo contrario aumenta la velocidad en 10 km/h
    def acelerar(self):
        if self.turbo:
            self.velocidadActual += 30
        else:
            self.velocidadActual += 10
    
    #definimos el metodo frenar el cual disminuye la velocidad del vehiculo en 5 km/h
    def frenar(self):
        self.velocidadActual -= 5

    
            
         
    
    @activarTurbo
    def hh(self):
        return "hola mundo"


            