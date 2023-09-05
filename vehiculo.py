class Vehiculo:
    #velocidadMaxima =0
    #capacidadTanque =0
    #definimos el contructor con sus respectivos atributos
    def __init__(self, velocidadMaxima, capacidadTanque):
        self.velocidadMaxima = velocidadMaxima
        self.capacidadTanque = capacidadTanque
        self.velocidadActual = 0
        self.nivelGasolina = capacidadTanque
    
    #definimos los metodos de acelerar y frenar  
    def acelerar(self):
        pass
    
    def frenar(self):
        pass    
    
    
    ''' def acelerar(self,cantidad):
        if self.velocidadActual + cantidad <= self.velocidadMaxima:
            self.velocidadActual +=cantidad
        else:
            self.velocidadActual = self.velocidadMaxima
    
    def frenar(self, cantidad):
        if self.velocidadActual -cantidad >= 0:
            self.velocidadActual -= cantidad
        else:
            self.velocidadActual = 0
    
    def cargarCombustible(self, cantidad):
        nivelActual = self.nivelGasolina + cantidad # 1+2----5
        if nivelActual <= self.capacidadTanque:
            self.nivelGasolina += cantidad
        else:
            self.nivelGasolina = self.capacidadTanque
    
    def consumirGasolina(self, distanciaRecorrida):
        gasolinaConsumida = distanciaRecorrida / 10
        if self.nivelGasolina >= gasolinaConsumida:
            self.nivelGasolina -= gasolinaConsumida
            return True
        else:
            return False '''
            
    

    
  

