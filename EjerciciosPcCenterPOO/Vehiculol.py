class Vehiculo:
    def moverse(self):
        pass
 
class Coche(Vehiculo):
    pass
 
class Bicicleta(Vehiculo):
    pass
 
# Crear instancias y llamar al método moverse
mi_coche = Coche()
mi_bicicleta = Bicicleta()
 
mi_coche.moverse()  # Salida esperada: "El coche se está moviendo"
mi_bicicleta.moverse()  # Salida esperada: "La bicicleta se está moviendo"