class Vehiculo:
    def __init__(self, tipo1, marca, modelo, año) :
        self.tipo1 = tipo1
        self.marca = marca 
        self.modelo = modelo
        self.año = año
    
    def info(self):
        print ("El vehiculo es un {} marca {}, modelo {} del año {} ".format(self.tipo1, self.marca, self.modelo, self.año))

class Coche (Vehiculo):
    def __init__(self, tipo1, marca, modelo, año, puertas):
        super().__init__(tipo1, marca, modelo, año)
        self.puertas = puertas
    
    def info(self):
        super().info()
        print ("Puertas:{} ".format(self.puertas))

class Motocicleta (Vehiculo):
    def __init__(self, tipo1, marca, modelo, año, tipo):
        super().__init__(tipo1, marca, modelo, año)
        self.tipo = tipo 

    def info(self):
        super().info()
        print ("Tipo:{} ".format(self.tipo))
    
coche = Coche ("Carro", "Toyota", "Yaris", 2024, 4)
motocicleta = Motocicleta ("motocicleta", "Honda" , "KTM 390", 2013, "deportivo" )

print ("Informacion del Vehiculo:")
coche.info()
motocicleta.info()