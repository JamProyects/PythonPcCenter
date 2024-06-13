class Animal:
    def hacer_sonido(self):
        raise NotImplementedError("Este método debe ser sobrescrito por las subclases")
 
class Perro(Animal):
    def hacer_sonido(self):
        return "Guau"

mi_perro = Perro()
print(mi_perro.hacer_sonido())