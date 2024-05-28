class Coche:
    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
    
    def informacion(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.anio}"

coche1 = Coche("Toyota", "Corolla", 2020)
print(coche1.informacion())

coche2 = Coche("Ford", "Mustang", 2022)
print(coche2.informacion())