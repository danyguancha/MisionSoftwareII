import random
import time

from coche import Coche
from moto import Moto


class Carrera:
    def simuladorCarrera(self,vehiculos, distancia):
        distanciaRecorrida =0
        while True:
            for vehiculo in vehiculos:
                vehiculo.acelerar()
                vehiculo.nivelGasolina -= 1
                if vehiculo.nivelGasolina <=0 :
                    print(f"El vehiculo {vehiculo.marca} {vehiculo.modelo} se quedo sin gasolina")
                    return  
                if vehiculo.velocidadActual <= vehiculo.velocidadMaxima:
                    distanciaRecorrida += vehiculo.velocidadActual
                if distanciaRecorrida >= distancia:
                    print(f"El vehiculo {vehiculo.marca} {vehiculo.modelo} ha ganado la carrera")
                    return
                #si el vehiculo reduce el combustible hasta 1 litro, se activa la posibilidad de frenar
                if random.randint(1, 10)==1:
                    vehiculo.frenar()
                
            print("---------------Estado de la carrera-----------------")
            for vehiculo in vehiculos:
                print(f"El vehiculo {vehiculo.marca} {vehiculo.modelo} va a {vehiculo.velocidadActual} km/h y tiene {vehiculo.nivelGasolina} litros de gasolina")   
            print("----------------------------------------------------")
            time.sleep(1)

salida = Carrera()
coche1 = Coche(200, 100, "Nissan", "Sentra", 100)
coche2 = Coche(300, 120, "Toyota", "Corolla", 100)
moto1 = Moto(150, 50, "Yamaha", "FZ", 50)
moto2 = Moto(200, 60, "Honda", "CBR", 50)
vehiculos = [coche1, coche2, moto1, moto2]

coche2.activarTurbo()

salida.simuladorCarrera(vehiculos, 1000)